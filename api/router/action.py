from http.client import HTTPException
from fastapi import APIRouter , Depends , status
from models import test , schemas
from models.database import engine , SessionLocal
from sqlalchemy.orm import Session

router = APIRouter()

test.Base.metadata.create_all(engine)

def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/blog' , status_code = status.HTTP_201_CREATED)
def create(request: schemas.Blog , db: Session = Depends(get_db)):
    new_blog = test.Blog(title=request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get('/blog_all')
def all(db: Session = Depends(get_db)):
    blogs = db.query(test.Blog).all()
    return blogs

@router.get('/blog/{id}' , status_code=200)
def show(id, db: Session= Depends(get_db)):
    blog = db.query(test.Blog).filter( test.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                                detail= f"Blog with the id {id} is not available")
    return blog


@router.delete('/deblog/{id}' , status_code = status.HTTP_204_NO_CONTENT)
def destroy(id , db: Session  = Depends(get_db)):
    blog = db.query(test.Blog).filter(test.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                                            detail=f"Blog with id {id} not found")
    blog.delete(synchronize_session=False)                                      
    db.commit()
    return "done"

@router.put('/uablog/{id}' , status_code= status.HTTP_202_ACCEPTED)
def update(id, request:schemas.Blog, db:Session= Depends(get_db)):
    blog = db.query(test.Blog).filter(test.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {id} not found")

    blog.update(request)
    db.commit()
    return "updated"