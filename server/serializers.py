from rest_framework import serializers

from .models import SmartFarmSensor, SmartFarm


class SmartFarmBaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartFarmSensor
        fields = '__all__'
        # exclude = ("")
    
class InfoListModelSerializer(SmartFarmBaseModelSerializer):
    class Meta(SmartFarmBaseModelSerializer.Meta):
        fields = [
                #   'sfid',
                  'remotepower',
                  'temperature',
                  'humidity']

class LedListModelSerializer(SmartFarmBaseModelSerializer):
    class Meta(SmartFarmBaseModelSerializer.Meta):
        fields = ['ledpower',
                  'ledstate',
                  'ledtoggle',
                  'ledautotoggle',
                  'ledstarttimevalue',
                  'ledstartminutevalue',
                  'ledendtimevalue',
                  'ledendminutevalue']

class WaterListModelSerializer(SmartFarmBaseModelSerializer):
    class Meta(SmartFarmBaseModelSerializer.Meta):
        fields = ['waterpumppower',
                'waterpumpstate',
                'waterpumptoggle',
                'waterpumpautotoggle',
                'waterpumpstarttime',
                'waterpumprunningtime',
                'waterlevelvoltage',
                'watertemperature']
class FanListModelSerializer(SmartFarmBaseModelSerializer):
    class Meta(SmartFarmBaseModelSerializer.Meta):
        fields = [
            'fanpower',
            'fanstate',
            'fantoggle',
            'fanautotoggle',
            'fanstarttimevalue',
            'fanstartminutevalue',
            'fanendtimevalue',
            'fanendminutevalue'
        ]

class DoorListModelSerializer(SmartFarmBaseModelSerializer):
    class Meta(SmartFarmBaseModelSerializer.Meta):
        fields = [
                'doorpower',
                'doorstate',
                'doortoggle',
                'doorautotoggle',
                'doorstarttimevalue',
                'doorstartminutevalue',
                'doorendtimevalue',
                'doorendminutevalue'
        ]

class WarningListModelSerializer(SmartFarmBaseModelSerializer):
    class Meta(SmartFarmBaseModelSerializer.Meta):
        fields = [
                'waterlevelwarning',
                'watertempwarning',
                'tempwarning',
                'humwarning',
                'soilwarning'
        ]

class SFSerializer(serializers.ModelSerializer):

    class Meta:
        model = SmartFarm
        fields = '__all__'