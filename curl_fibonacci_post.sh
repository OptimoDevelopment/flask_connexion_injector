#!/bin/bash

curl -XPOST http://localhost:5000/api/v1.0/fibonacci -H "Content-Type: application/json" -d '{"index": 10}'
