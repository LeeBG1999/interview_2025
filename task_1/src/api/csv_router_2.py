# ...existing code...
from fastapi import APIRouter, File, UploadFile, status
from fastapi.responses import JSONResponse
import pandas as pd
import tempfile
import shutil
import os
from starlette.concurrency import run_in_threadpool

from src.utils.utils import calculate_statistics

router = APIRouter()

@router.post("/generateReport")
async def upload_csv(file: UploadFile = File(...)):
    # validate file extension
    if not file.filename.lower().endswith('.csv'):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"error": "File must be a CSV."}
        )

    tmp_path = None
    try:
        # stream upload to a temporary file to avoid loading entire file into memory
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
        tmp_path = tmp.name
        # copyfileobj is blocking — run in threadpool
        await run_in_threadpool(shutil.copyfileobj, file.file, tmp)
        tmp.flush()
        tmp.close()

        # read CSV with pandas in threadpool
        df = await run_in_threadpool(pd.read_csv, tmp_path)

        # run heavy computation in threadpool as well
        result = await run_in_threadpool(calculate_statistics, df)

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": "CSV processed successfully", "data": result}
        )

    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"error": "Failed to process CSV", "details": str(e)}
        )

    finally:
        # cleanup
        try:
            file.file.close()
        except Exception:
            pass
        if tmp_path and os.path.exists(tmp_path):
            try:
                os.unlink(tmp_path)
            except Exception:
                pass
