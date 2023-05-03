

#    <1й способо реализации АПИ вью вывода - через методы, где прописываем каждый метод вручную, самый базовый>
# class UnitsAPIView(generics.ListAPIView):
#     queryset = Unitsdb.objects.all()
#     serializer_class = UnitSerializer
# class UnitsAPIView(APIView):
#     def get(self, request):
#         lst = Unitsdb.objects.all()
#         return Response({'posts':UnitSerializer(lst, many=True).data})
#     def post(self,request):
#         serializer = UnitSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#         # post_new = Unitsdb.objects.create(
#         #     name=request.data['name'],
#         #     fr=request.data['fr'],
#         #     type=request.data['type'],
#         #     short_des=request.data['short_des'],
#         #     des=request.data['des'],
#         # )
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Unitsdb.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#
#         serializer = UnitSerializer(data=request.data, instance = instance)
#         serializer.is_valid(raise_exception = True)
#         serializer.save()
#         return Response({"data": serializer.data})
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#         try:
#             instance = Unitsdb.objects.get(pk=pk)
#             instance.delete()
#         except:
#             return Response({"error": "Object does not exists"})
#
#         return Response({"post": "delete post" + str(pk)})




#    <2й способо реализации АПИ вью вывода - через классы, где впервые реализуем свой сериализатор, лучше первого, но не так практичен как 3й>
# class UnitsAPIList(generics.ListCreateAPIView):
#     queryset = Unitsdb.objects.all()
#     serializer_class = UnitSerializer
#     permission_classes = (IsAdminOrReadOnly,)
#
# class UnitsAPIUpdate(generics.RetrieveUpdateAPIView):
#     queryset = Unitsdb.objects.all()
#     serializer_class = UnitSerializer
#     #permission_classes = (IsAdminOrReadOnly,)
#
# class UnitsAPIDestroy(generics.RetrieveDestroyAPIView):
#     queryset = Unitsdb.objects.all()
#     serializer_class = UnitSerializer
#     permission_classes = (IsAdminOrReadOnly,)
#
# class UnitsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Unitsdb.objects.all()
#     serializer_class = UnitSerializer
#     # permission_classes = (IsAdminOrReadOnly,)