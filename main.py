#installation Step 
#if you want to install fastapi in your machine follow this link:
#https://fastapi.tiangolo.com/

# FastApi basic path knowledge

from fastapi import FastAPI

# same as express
app =FastAPI()

@app.get('/') #path('/') & get method is operatin

#def is the keyword for defining a function
#index is path operation function
def index():return {
    'info':'FastApi get method',
     'data':{
         'name':'Ashish'
     }
}
@app.get('/about')
def about():
    return {'data':'about page' }
    

