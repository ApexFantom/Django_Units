# def encode():
#     model = UnitModel('Archon', 'P', 'Massive psionic', 'des','DESCRIPTION', '', '')
#     model_sr = UnitSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"title":"1"}')
#     data = JSONParser().parse(stream)
#     seializer = UnitSerializer(data=data)
#     seializer.is_valid()
#     print(serializer.validated_data)