
#importing the sqlachemy library
from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker, Session


#importing the fastapi library
from fastapi import FastAPI, Depends
from pydantic import BaseModel

#defining the basic model
class Base(DeclarativeBase):
    pass

#a class for creating the main columns of a database
class Book(Base):
    __tablename__ = "Book"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    author: Mapped[str] = mapped_column()
    year: Mapped[int] = mapped_column()


#the database connection object
engine = create_engine("sqlite:///book_api/book.db", echo=True)
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#a function for determining the successful connection to the database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from FastAPI!"}

class BookIn(BaseModel):
    title: str
    author: str
    year: int

class BooksOut(BaseModel):
    id: int
    title: str
    author: str
    year: int

@app.post("/books/", response_model=BooksOut)
def post_books(book_data: BookIn, db: Session = Depends(get_db)):
    new_book = Book(
        title=book_data.title,
        author=book_data.author,
        year=book_data.year
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book) 
    return new_book

@app.get("/books/", response_model=list[BooksOut])
def get_books(db: Session = Depends(get_db)):
    books = db.query(Book).all()
    return books  

@app.delete("/books/{book_id}")
def delete_books(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        return {"message": "Book not found"}
    db.delete(book)
    db.commit()
    return {"message": "Book deleted"}

@app.put("/books/{book_id}", response_model=BooksOut)
def update_books(book_id: int, book_data: BookIn, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        return {"message": "Book not found"}
    book.title = book_data.title
    book.author = book_data.author
    book.year = book_data.year
    db.commit()
    db.refresh(book)
    return book

@app.get("/books/search", response_model=list[BooksOut])
def search_books(title: str = None, author: str = None, year: int = None, db: Session = Depends(get_db)):
    query = db.query(Book)
    if title:
        query = query.filter(Book.title.contains(title))
    if author:
        query = query.filter(Book.author.contains(author))
    if year:
        query = query.filter(Book.year == year)
    books = query.all()
    return books
