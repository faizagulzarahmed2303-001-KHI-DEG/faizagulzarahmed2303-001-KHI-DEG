#!/bin/bash

sudo docker compose exec broker kafka-topics --create --topic messages --bootstrap-server broker:9092
