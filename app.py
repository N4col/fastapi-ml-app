from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError
from typing import Any
from model import model  # Importujemy model z osobnego pliku
import numpy as np

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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
