from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .models import Request
from .serializers import CreateRequestSerializer, ListRequestSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import  status
from django.contrib.auth import  authenticate, login
import json




class UserLoginView(APIView):
    permission_classes=()

    def post(self, request):
        
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login(request, user)
            data = UserSerializer(user)
            return Response({
                "status":status.HTTP_200_OK,
                "message":"Login Successful",
                "user_id":user.id,
                "user_email":user.email,
                "user_username":user.username
            })
        else:
            return Response(
                {
                    "status":status.HTTP_400_BAD_REQUEST,
                    "message":"Sorry, no user was found with the username or password you entered"
                }
            )

class CreateRequestView(CreateAPIView):
    permission_classes=()
    queryset=Request.objects.all()
    serializer_class = CreateRequestSerializer


class ListRequestsForARequester(APIView):
    permission_classes=()

    def get(self, request, username):
        requests =Request.objects.filter(username=username)
        data = ListRequestSerializer(requests, many=True).data

        return Response({
            "status":status.HTTP_200_OK,
            "data":data
        }, status=status.HTTP_200_OK)


class RetriveRequest(APIView):
    permission_classes=()

    def get(self, request, id):
        request_ = Request.objects.get(id=id)

        data = ListRequestSerializer(request_).data

        return Response({
            "status":status.HTTP_200_OK,
            "data":data
        }, status=status.HTTP_200_OK)


class ApproveDenyRequestInterControl(APIView):
    permission_classes=()

    def put(self, request, id):
        request_ = Request.objects.get(id=id)

        value = request.data['value']

        value_ = {
            "Deny":False,
            "Approve":True,
            
        }

        status_ = {
            "Deny":"Denied",
            "Approve":"Approved"
        }
        

        res = {
            "Deny":"Request has been denied.",
            "Approve":"Request has been approved."
        }



        request_.approved_by_internal_control = value_[value]
        request_.internal_control_comment = request.data['comment']
        request_.request_status = status_[value]
        request_.save()
        

        # OTHER THINGS


        return Response(
            {
                "status":status.HTTP_200_OK,
                "message":res[value]
            }, status=status.HTTP_200_OK
        )



class ApproveDenyRequestZonal(APIView):
    permission_classes=()

    def put(self, request, id):
        request_ = Request.objects.get(id=id)

        value_ = {
            "Deny":False,
            "Approve":True,
        }
        status_ = {
            "Deny":"Denied",
            "Approve":"Approved"
        }

        res = {
            "Deny":"Request has been denied.",
            "Approve":"Request has been approved."
        }

        value = request.data['value']

        comment = request.data['comment']



        request_.approved_by_zonal = value_[value]
        request_.zonal_comment = comment
        request_.request_status = status_[value]
        request_.save()

        # OTHER THINGS
        # Setting zonal email


        return Response(
            {
                "status":status.HTTP_200_OK,
                "message":res[value]
            }, status=status.HTTP_200_OK
        )


class ApproveDenyRequestLineManager(APIView):
    permission_classes=()

    def put(self, request, id, ):
        request_ = Request.objects.get(id=id)
        value = request.data['value']

        value_ = {
            "Deny":False,
            "Approve":True,
        }

        res = {
            "Deny":"Request has been denied.",
            "Approve":"Request has been approved."
        }

        status_ = {
            "Deny":"Denied",
            "Approve":"Approved"
        }

        comment = request.data['comment']



        request_.approved_by_line_manager = value_[value]
        request_.internal_control_comment = comment
        request_.request_status = status_[value]
        request_.save()

        # OTHER THINGS
        # Setting zonal email


        return Response(
            {
                "status":status.HTTP_200_OK,
                "message":res[value]
            }, status=status.HTTP_200_OK
        )


class RetrieveZonalRequestsView(APIView):
    permission_classes=()

    def get(self, request,email):

        try:
            requests_ = Request.objects.filter(zonal=email).order_by('-date_posted')

            data = ListRequestSerializer(requests_, many=True)

            # data.is_valid(raise_exception=True)

            return Response({
                "status":status.HTTP_200_OK,
                "data":data.data
            }
            )
        except  Exception as e:
            print(e)

            return Response({
                "status":status.HTTP_400_BAD_REQUEST,
                "message":"Sorry something went wrong."
            })


class RetrieveLineManagerRequestsView(APIView):
    permission_classes=()

    def get(self, request,email):

        try:
            requests_ = Request.objects.filter(line_manager=email).order_by('-date_posted')

            data = ListRequestSerializer(requests_, many=True)

            # data.is_valid(raise_exception=True)

            return Response({
                "status":status.HTTP_200_OK,
                "data":data.data
            }
            )
        except  Exception as e:
            print(e)

            return Response({
                "status":status.HTTP_400_BAD_REQUEST,
                "message":"Sorry something went wrong."
            })



class RetrieveInternalControlRequestsView(APIView):
    permission_classes=()

    def get(self, request):

        try:
            requests_ = Request.objects.all().order_by('-date_posted')

            data = ListRequestSerializer(requests_, many=True)

            # data.is_valid(raise_exception=True)

            return Response({
                "status":status.HTTP_200_OK,
                "data":data.data
            }
            )
        except  Exception as e:
            print(e)

            return Response({
                "status":status.HTTP_400_BAD_REQUEST,
                "message":"Sorry something went wrong."
            })








         

