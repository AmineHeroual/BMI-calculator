from fastapi import FastAPI, Query
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware


class BMIOutput(BaseModel):
    bmi: float
    message: str


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")

def Hi():
    return {"message": "Hello python"}

@app.get("/calculate_bmi")

def calculate_bmi(
    weight: float= Query(..., gt=20,lt=200, description="Weight in kg"),
    height:float= Query(..., gt=1,lt=3, description="height in m")
     ):
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        msg = "لديك نقص في الوزن كل اكثر ياصديقي"
    elif 18.5 <= bmi < 25:
        msg = "وزنك جيد حافظ عليه"
    elif 25 <= bmi < 30:
        msg = "لديك زيادة في الوزن تمرن اكثر"
    else: 
        msg = "تعاني من السمنة راجع طبيب مختص"


    return BMIOutput(bmi=bmi, message=msg)