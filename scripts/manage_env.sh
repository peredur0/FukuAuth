#!/bin/bash

set -e

ENV=$1
CMD=$2

if [[ -z "$ENV" || -z "$CMD" ]]; then
    echo "Usage: .scripts/manage_env.sh [test|prod] [start|stop]"
    exit 1
fi

case "$ENV" in
    test)
        COMPOSE_FILE="./infra/compose.test.yaml"
        ;;
    prod)
        COMPOSE_FILE="./infra/compose.yaml"
        ;;
    *)
        echo "Unknown environment: $ENV"
        echo "Allowed environment: test, prod"
        exit 1
        ;;
esac

case "$CMD" in
    start)
        echo "Starting $ENV environment"
        docker compose -f "$COMPOSE_FILE" up -d
        ;;
    stop)
        echo "Starting $ENV environment"
        docker compose -f "$COMPOSE_FILE" down
        ;;
    *)
        echo "Unknown command: $CMD"
        echo "Allowed commands: start, stop"
        exit 1
        ;;
esac
