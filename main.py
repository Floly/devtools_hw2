from fastapi import FastAPI, HTTPException, Response
from models import Dog, Timestamp,DogType

app = FastAPI()

dogs_db = {
    0: Dog(name='Bob', pk=0, kind='terrier'),
    1: Dog(name='Marli', pk=1, kind="bulldog"),
    2: Dog(name='Snoopy', pk=2, kind='dalmatian'),
    3: Dog(name='Rex', pk=3, kind='dalmatian'),
    4: Dog(name='Pongo', pk=4, kind='dalmatian'),
    5: Dog(name='Tillman', pk=5, kind='bulldog'),
    6: Dog(name='Uga', pk=6, kind='bulldog')
}

post_db = [
    Timestamp(id=0, timestamp=12),
    Timestamp(id=1, timestamp=10)
]

@app.get('/')
def root__get():
    return {"message": "Hello World"}

@app.get('/post')
def get_post_post_post():
    return post_db[-1]

@app.get('/dog', response_model=Dog, summary='Get Dogs')
def get_dogs_dog_get(kind: DogType):
    if kind in ['terrier', 'bulldog', 'dalmatian']:
        ret_list = []

        for f in dogs_db.values():
            if f.kind == kind:
                ret_list.append(f)

        return ret_list[0]

    else:
        raise HTTPException(status_code=422, 
                            detail='This dog type doesn`t exists')

@app.post('/dog', response_model=Dog, summary='Create Dog')
def create_dog_dog_post(dog: Dog):
    existing_pk = [dog.pk for dog in dogs_db.values()]
    if dog.pk in existing_pk:
        raise HTTPException(status_code=409,
                            detail='The specified PK already exists.')
    else:
        dogs_db.update({dog.pk: dog})
        return dog

@app.get('/dog/{pk}', response_model=Dog, summary='Get Dog By Pk')
def get_dog_by_pk(pk: int):
    if pk in dogs_db.keys():
        return dogs_db[pk]

    else: 
        raise HTTPException(status_code=422, 
                            detail='This dog doesn`t exist')
    
@app.patch('/dog/{pk}', response_model=Dog, summary='Update Dog')
def update_dog_dog__pk__patch(pk: int, dog:Dog):
    if pk in dogs_db.keys():
        dog.pk = pk
        dogs_db[pk] = dog
        return dog