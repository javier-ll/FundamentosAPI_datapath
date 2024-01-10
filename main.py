import uvicorn
from fastapi import FastAPI

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from pydantic import BaseModel
from typing import Union, Optional
from constants import FAKE_DB_PEOPLE

people_list=list()
people_list.extend(FAKE_DB_PEOPLE)

class Person (BaseModel):
    name: str
    language: str
    id: Optional [str] = None
    bio: str
    version: float

def find_index_by_id(person_id):
    _index=None
    for index, value in enumerate(people_list):
        if value['id']==person_id:
            _index=index
            break
    return _index

app=FastAPI()

@app.get(path='/api/people/get_all')
async def get_people(language: Union[str,None]=None):
    response=people_list
    if language:
        response=list(filter(lambda x: x['language']==language, people_list))
    return JSONResponse(content=response, status_code=200)

@app.get(path='/api/people/{person_id}')
async def get_person(person_id: str):
    response=None
    for person in people_list:
        if person['id']==person_id:
            response=person
            status_code=200
            break
    return JSONResponse(content=response, status_code=status_code)

@app.post(path='/api/people')
async def create_person(person: Person):
    person_id=person.id
    if person_id is None:
        person.id=f'{person.name}.{person.language}.{person.bio}.{person.version}'
    people_list.append(person.dict())
    json_data=jsonable_encoder(person)
    return JSONResponse(content=json_data, status_code=201)

@app.put(path='/api/people/{person_id}')
async def update_person(person_id:str,person:Person):
    if person.id is None:
        person.id=f'{person.name}.{person.language}.{person.bio}.{person.version}'
    index_update=find_index_by_id(person_id=person_id)
    if index_update is None:
        return JSONResponse(content=None,status_code=404)
    else:
        people_list[index_update]=person.dict()
    return JSONResponse(content=True,status_code=200)

@app.delete(path='/api/people/{person_id}')
async def delete_person(person_id: str):
    index_delete=find_index_by_id(person_id=person_id)
    if index_delete is None:
        return JSONResponse(content=None,status_code=404)
    else:
        people_list.pop(index_delete)
    return JSONResponse(content=True,status_code=200)