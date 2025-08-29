Data Overview



This document provides an overview of the dataset used in SentinelNet for predictive structural health monitoring.



Dataset Sources



Acoustic Emission (AE) Sensor Data



Collected using piezoelectric sensors.



Captures micro-crack formation signals.



Simulated/Benchmark Data



Public datasets from structural health monitoring research papers.



Edge Impulse sample datasets for training and validation.



Data Format



Time-series signals



Sampled at different frequencies depending on the sensor.



Stored in .csv format for preprocessing.



Labels



0 → Normal condition



1 → Micro-crack detected



Data Collection Setup



Hardware



ESP32 microcontroller with Wi-Fi capability.



Piezoelectric AE sensors connected via signal conditioning circuit.



Software



Data streamed to Edge Impulse for preprocessing.



Data stored in local .csv files for backup and model retraining.



Preprocessing Steps



Noise filtering (removal of unwanted environmental noise).



Normalization of signal amplitude.



Feature extraction (FFT, RMS, waveform energy).



Segmentation into fixed-length windows.



Example Data Snapshot

Time (ms)	Signal Amplitude	Label

0.00	0.012	0

0.01	0.018	0

0.02	0.256	1

0.03	0.341	1

