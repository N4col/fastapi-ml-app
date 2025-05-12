from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError
from typing import Any
from model import model  
import numpy as np
import os

app = FastAPI()


class PredictRequest(BaseModel):
    value: float


@app.get("/")
def read_root() -> dict[str, Any]:
    return {"message": "Hello, world!"}


@app.get("/info")
def get_info() -> dict[str, Any]:
    return {
        "model_type": "LinearRegression",
        "number_of_features": 1
    }


@app.get("/health")
def health_check() -> dict[str, Any]:
    return {"status": "ok"}


@app.post("/predict")
def predict(data: PredictRequest) -> dict[str, Any]:
    try:
        if data.value is None:
            raise HTTPException(status_code=400, detail="Wartość 'value' jest wymagana.")

        prediction = model.predict(np.array([[data.value]]))[0]
        return {"prediction": prediction.item()}
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=f"Błąd walidacji danych: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Nieoczekiwany błąd: {str(e)}")



@app.get("/config")
def read_config():
    config_value = os.getenv("MY_CONFIG_VALUE", "Brak wartości")
    return {"config": config_value}



if __name__ == "__main__":
    import uvicorn
    import os

    port = int(os.environ.get("PORT", 8080))  # Zmienna środowiskowa z Google Cloud Run
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True)

