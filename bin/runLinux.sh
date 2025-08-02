#!/bin/bash

# ╭───────────────────────────────╮
# │ ENVIRONMENT DIR/ENVRC SETUP   │
# ╰───────────────────────────────╯
if [ ! -f ".envrc" ]; then
    echo "Creating .envrc..."
    cat << EOF > .envrc
layout python3
export VIRTUAL_ENV=\$(pwd)/.venv
export PATH=\$VIRTUAL_ENV/bin:\$PATH
EOF
fi

if [ ! -d ".direnv" ]; then
    echo "Creating .direnv directory..."
    mkdir .direnv
fi

python3 -m venv .venv > /dev/null 2>&1

# Activate direnv
eval "$(direnv export bash)"
direnv allow

# ╭──────────────────────╮
# │ INSTALL DEPENDENCIES │
# ╰──────────────────────╯
pip3 install -r requirements.txt > /dev/null 2>&1
pip install -e . > /dev/null 2>&1

# ╭────────────────────────────╮
# │ PROMPT: CHOOSE FILE        │
# ╰────────────────────────────╯
pip install cython numpy
python3 src/setup.py build_ext --inplace
