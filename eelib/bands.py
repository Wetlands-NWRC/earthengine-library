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


class S2DCParsed(Enum):
    """After a band offset has been added and Composite has been parsed into
    seperate Seasonal Composites"""
    B1 = 'Aerosols'
    B2 = 'Blue'
    B3 = 'Green'
    B4 = 'Red'
    B5 = 'Red Edge 1'
    B6 = 'Red Edge 2'
    B7 = 'Red Edge 3'
    B8 = 'NIR'
    B9 = 'Red Edge 4'
    B10 = 'SWIR 1'
    B11 = 'SWIR 2'


class S2DataCube(Enum):
    """Original Data Cube Band Mappings"""
    pass
