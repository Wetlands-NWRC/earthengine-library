import ee

from eelib.scripttools import moa


def test_moa_table_export():
    image = ee.Image(
        'users/ryangilberthamilton/BC/williston/stacks/WillistonA_2018')
    label_column = 'cDesc'
    pts = ee.FeatureCollection(
        'users/ryangilberthamilton/BC/williston/fpca/willistonA_no_floodplain')

    moaScores = moa(
        image,
        label_col=label_column,
        pts=pts
    )

    task = ee.batch.Export.table.toDrive(
        collection=moaScores,
        description='moa_script_tool_test',
        folder='MOAScores',
        fileFormat='CSV'
    )
    task.start()


if __name__ == "__main__":
    test_moa_table_export()
