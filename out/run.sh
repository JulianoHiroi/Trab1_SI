#!/bin/bash

# Número de repetições
N=0

# Loop for para repetir os comandos
for ((i=0; i<=$N; i++)); do
  python graficoTempera.py dataResultados/data_0.9_1000/teste_$i.txt &
done