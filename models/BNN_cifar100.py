from nnUtils import *

model = Sequential([
    BinarizedWeightOnlySpatialConvolution(128,3,3,1,1, padding='VALID', bias=False),
    BatchNormalization(),
    HardTanh(),
    BinarizedSpatialConvolution(128,3,3, padding='SAME', bias=False),
    SpatialMaxPooling(2,2,2,2),
    BatchNormalization(),
    HardTanh(),
    BinarizedSpatialConvolution(256,3,3, padding='SAME', bias=False),
    BatchNormalization(),
    HardTanh(),
    BinarizedSpatialConvolution(256,3,3, padding='SAME', bias=False),
    SpatialMaxPooling(2,2,2,2),
    BatchNormalization(),
    HardTanh(),
    BinarizedSpatialConvolution(512,3,3, padding='SAME', bias=False),
    BatchNormalization(),
    HardTanh(),
    BinarizedSpatialConvolution(512,3,3, padding='SAME', bias=False),
    SpatialMaxPooling(2,2,2,2),
    BatchNormalization(),
    HardTanh(),
    BinarizedAffine(1024, bias=False),
    BatchNormalization(),
    HardTanh(),
    BinarizedAffine(1024, bias=False),
    BatchNormalization(),
    HardTanh(),
    BinarizedAffine(100),  # cifar100和cifar10只是这里不一样，cifar10此处为10
    BatchNormalization()
])
