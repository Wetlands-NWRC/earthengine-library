from enum import Enum


class S2TOA(Enum):
    B1 = 'Aerosols'
    B2 = 'Blue'
    B3 = 'Green'
    B4 = 'Red'
    B5 = 'Red Edge 1'
    B6 = 'Red Edge 2'
    B7 = 'Red Edge 3'
    B8 = 'NIR'
    B8A = 'Red Edge 4'
    B9 = 'Water vapor'
    B10 = 'Cirrus'
    B11 = 'SWIR 1'
    B12 = 'SWIR 2'


class S2SR(Enum):
    B1 = 'Aerosols'
    B2 = 'Blue'
    B3 = 'Green'
    B4 = 'Red'
    B5 = 'Red Edge 1'
    B6 = 'Red Edge 2'
    B7 = 'Red Edge 3'
    B8 = 'NIR'
    B8A = 'Red Edge 4'
    B11 = 'SWIR 1'
    B12 = 'SWIR 2'


class S2DC(Enum):
    B0 = 'Aerosols'
    B1 = 'Blue'
    B2 = 'Green'
    B3 = 'Red'
    B4 = 'Red Edge 1'
    B5 = 'Red Edge 2'
    B6 = 'Red Edge 3'
    B7 = 'NIR'
    B8 = 'Red Edge 4'
    B9 = 'SWIR 1'
    B10 = 'SWIR 2'
