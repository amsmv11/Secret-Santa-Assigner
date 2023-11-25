#!/usr/bin/env sh
set -ex


LINE_LENGTH=120

BLACK_ARGS=""
if [ "$1" = "check" ];then
    BLACK_ARGS="--check"
    ISORT_ARGS="--check-only"
fi

# Run  isort, flake8, black, pylint and mypy on all files

isort --profile black -w ${LINE_LENGTH} ${ISORT_ARGS} src/ main.py
if [ $? -ne 0 ];
then
    echo "isort failed ❌"
    exit 1
fi
echo "isort ✅"


# Changing the default exclusion list because it was excluding the 'pytype' dir
black ${BLACK_ARGS} -l ${LINE_LENGTH} --target-version py310 --exclude "(\.eggs|\.git|\.hg|\.mypy_cache|\.nox|\.tox|\.venv|_build|buck-out|dist|env|.pytype|venv)" .
if [ $? -ne 0 ];
then
    echo "Black failed ❌"
    exit 1
fi
echo "Black ✅"

flake8  --max-line-length ${LINE_LENGTH} --ignore E203,W503 src/ main.py
if [ $? -ne 0 ];
then
    echo "Flake8 failed ❌"
    exit 1
fi
echo "Flake8 ✅"

mypy .
if [ $? -ne 0 ];
then
    echo "Mypy failed ❌"
    exit 1
fi
echo "Mypy ✅"

find . -type f -name "*.py" -not -path "*streamlit_pydantic*" | xargs pylint --max-line-length ${LINE_LENGTH}
if [ $? -ne 0 ];
then
    echo "Pylint failed ❌"
    exit 1
fi
echo "Pylint ✅"

exit 0
