#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset


celery -A seguros.taskapp worker -l INFO