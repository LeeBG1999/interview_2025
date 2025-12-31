from fastapi import APIRouter, File, UploadFile, status
from fastapi.responses import JSONResponse
import pandas as pd
from io import StringIO

from src.utils.utils import calculate_statistics


csv_router = APIRouter()
@csv_router.post("/generateReport")
async def upload_csv(file: UploadFile = File(...)):
    
    # check the file type
    if not file.filename.endswith('.csv'):
        return JSONResponse(
                status_code=status.HTTP_417_EXPECTATION_FAILED,
                content= {"error": "File must be a CSV."}
                )
    
    # receieve data and merge into dataframe
    contents = await file.read()
    decoded = contents.decode("utf-8")
    df = pd.read_csv(StringIO(decoded))

    
    # calculate statistics
    result = calculate_statistics(df)

    return JSONResponse(
                status_code=status.HTTP_200_OK,
                content= {
                    "message": "CSV processed successfully", 
                    "data": result}
                )


