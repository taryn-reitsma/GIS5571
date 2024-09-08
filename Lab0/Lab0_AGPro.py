from arcgis.gis import GIS
gis = GIS("home")

roads = gis.content.get("4352f7fce3564b33bb147b51c5d7a53a")
roads

from arcgis import features
roads_buffer = features.analysis.create_buffers(input_layer=roads,
                         distances=[50],
                         side_type ='Full',
                         units='Meters',
                         end_type='Round',
                         output_name='RiceCounty50m_AGProBuffer')

roads_buffer


