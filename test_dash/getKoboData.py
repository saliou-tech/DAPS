import pandas as pd
import re 
from koboextractor import KoboExtractor

class GetKoboData:

    def __init__(self):
        self.KOBO_TOKEN="195930fa6955af494ccd95acc9d8e5e8e51e2796"
        self.kobo = KoboExtractor(self.KOBO_TOKEN, 'https://kobo.humanitarianresponse.info/api/v2', debug=True)


    def getAllData(self):
        assets = self.kobo.list_assets()
        print("A")
        asset_uid = assets['results'][0]['uid']
        print("B")
        asset = self.kobo.get_asset(asset_uid)
        print("C")
        choice_lists = self.kobo.get_choices(asset)
        print("D")
        questions = self.kobo.get_questions(asset=asset, unpack_multiples=True)
        asset_data = self.kobo.get_data(asset_uid)
        results = self.kobo.sort_results_by_time(asset_data['results'])
        labeled_results = []
        for result in results:
            labeled_results.append(self.kobo.label_result(unlabeled_result=result, choice_lists=choice_lists, questions=questions, unpack_multiples=True))
            
        return labeled_results


    def getDapsDataFrame(self,labeled_results):
        N0,A1,A2,A3,A4,A5,A6= [],[],[],[],[],[] ,[]
        Bo,Bo1,B1,B2,B3,B4,B4_001,B5,B6,B8,B10=[],[],[],[],[],[],[] ,[],[],[],[]
        #############SECTION3 : IDENTIFICATION DES MEMBRES DU BUREAU DE LA FEDERATION OU DU GROUPEMENT SPORTIF###
        C1,C2,C3,C5,C6,C7,C8,C9,C10= [],[],[],[],[],[] ,[],[] ,[] 
        ############################SECTION 4 : COMPOSITION ET SITUATION DES FEDERATIONS ET REGROUPEMENTS SPORTIFS
        D1,D2,D3,D4,D5,D5_001,D5_002,D6,D6_001,D6_002,D7_003,D7_004,D7_005,D7_006=[],[],[],[],[],[],[],[],[],[],[],[],[],[]
        D8,D9,D10,D11,D12,D15,D16,D17,D18,D18_001,D19,D20=[],[],[],[],[],[],[],[],[],[],[],[]
        D21,D22,D23,D24,D25,D26,D27,D28,D29,D30,D31,D32=[],[],[],[],[],[],[],[],[],[],[],[]
        D33,D34,D35,D36,D37,D38,D39,D40,D41,D42,D43=[],[],[],[],[],[],[],[],[],[],[]
        ##########SECTION 5 : COMPETITIONS
        E1,E2,E3,E4,E5,E6,E7,E8,E9,E10,E11,E12,E13,E13_001,E13_002,E14,E15,E16,E18,HF=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]

        for i in range(0 ,len(labeled_results)):
            N0.append(labeled_results[i]['results']['No']['answer_label'])
            A1.append(labeled_results[i]['results']['A1']['answer_label'])
            A2.append(labeled_results[i]['results']['A2']['answer_label'])
            A3.append(labeled_results[i]['results']['A3']['answer_label'])
            A4.append(labeled_results[i]['results']['A4']['answer_label'])
            A5.append(labeled_results[i]['results']['A5']['answer_label'])
            A6.append(labeled_results[i]['results']['A6']['answer_label'])
            #############section 2########################################
            Bo.append(labeled_results[i]['results']['Bo']['answer_label'])
            Bo1.append(labeled_results[i]['results']['Bo1']['answer_label'])
            B1.append(labeled_results[i]['results']['B1']['answer_label'])
            B2.append(labeled_results[i]['results']['B2']['answer_label'])
            B3.append(labeled_results[i]['results']['B3']['answer_label'])
            B4.append(labeled_results[i]['results']['B4']['answer_label'])
            B4_001.append(labeled_results[i]['results']['B4_001']['answer_label'])
            B5.append(labeled_results[i]['results']['B5']['answer_label'])
            B6.append(labeled_results[i]['results']['B6']['answer_label'])
            B8.append(labeled_results[i]['results']['B8']['answer_label'])
            if(labeled_results[i]['results']['B8']['answer_label']=="NON"):
                B10.append("NA") 
            else:
                B10.append(labeled_results[i]['results']['B10']['answer_label'])
        ###########SECTION3 : IDENTIFICATION DES MEMBRES DU BUREAU DE LA FEDERATION OU DU GROUPEMENT SPORTIF####""
            C1.append(labeled_results[i]['results']['C1']['answer_label'])
            C2.append(labeled_results[i]['results']['C2']['answer_label'])
            C3.append(labeled_results[i]['results']['C3']['answer_label'])
            C5.append(labeled_results[i]['results']['C5']['answer_label'])
            C6.append(labeled_results[i]['results']['C6']['answer_label'].strip())
            C7.append(labeled_results[i]['results']['C7']['answer_label'])
            C8.append(labeled_results[i]['results']['C8']['answer_label'].strip())
            C9.append(labeled_results[i]['results']['C9']['answer_label'])
            C10.append(labeled_results[i]['results']['C10']['answer_label'])
        ############################SECTION 4 : COMPOSITION ET SITUATION DES FEDERATIONS ET REGROUPEMENTS SPORTIFS
            D1.append(labeled_results[i]['results']['D1']['answer_label'])
            D2.append(labeled_results[i]['results']['D2']['answer_label'])
            D3.append(labeled_results[i]['results']['D3']['answer_label'])
            if(labeled_results[i]['results']['D3']['answer_label']=="Non"):
                D4.append("NA")
            else:
                D4.append(labeled_results[i]['results']['D4']['answer_label'])
            D5.append(labeled_results[i]['results']['D5']['answer_label'])
            if(labeled_results[i]['results']['D5']['answer_label']=="Non"):
                D5_001.append("NA")
            else:
                D5_001.append(labeled_results[i]['results']['D5_001']['answer_label'])
            D5_002.append(labeled_results[i]['results']['D5_002']['answer_label'])
            D6.append(labeled_results[i]['results']['D6']['answer_label'])
            if(labeled_results[i]['results']['D6']['answer_label']=="Non"):
                D6_001.append("NA")
                D6_002.append("NA")

            else:
                D6_001.append(labeled_results[i]['results']['D6_001']['answer_label'])
                D6_002.append(labeled_results[i]['results']['D6_002']['answer_label'])
            D7_003.append(labeled_results[i]['results']['D7_003']['answer_label'])
            if(labeled_results[i]['results']['D7_003']['answer_label']=="Non"):
                D7_004.append("NA")

            else:
                D7_004.append(labeled_results[i]['results']['D7_004']['answer_label'])
                
            D7_005.append(labeled_results[i]['results']['D7_005']['answer_label'])
            if(labeled_results[i]['results']['D7_005']['answer_label']=="Non"):
                D7_006.append("NA")
            else:
                D7_006.append(labeled_results[i]['results']['D7_006']['answer_label'])

            D8.append(labeled_results[i]['results']['D8']['answer_label'])
            D9.append(labeled_results[i]['results']['D9']['answer_label'])
            D10.append(labeled_results[i]['results']['D10']['answer_label'])
            D11.append(labeled_results[i]['results']['D11']['answer_label'])
            D12.append(labeled_results[i]['results']['D12']['answer_label'])
            D15.append(labeled_results[i]['results']['D15']['answer_label'])
            D16.append(labeled_results[i]['results']['D16']['answer_label'])
            D17.append(labeled_results[i]['results']['D17']['answer_label'])
            D18.append(labeled_results[i]['results']['D18']['answer_label'])
            D18_001.append(labeled_results[i]['results']['D18_001']['answer_label'])
            D19.append(labeled_results[i]['results']['D19']['answer_label'])
            D20.append(labeled_results[i]['results']['D20']['answer_label'])
            #D10.append(labeled_results[i]['results']['D3']['answer_label'])
            D21.append(labeled_results[i]['results']['D21']['answer_label'])
            D22.append(labeled_results[i]['results']['D22']['answer_label'])
            D23.append(labeled_results[i]['results']['D23']['answer_label'])
            D24.append(labeled_results[i]['results']['D24']['answer_label'])
            D25.append(labeled_results[i]['results']['D25']['answer_label'])
            D26.append(labeled_results[i]['results']['D26']['answer_label'])
            D27.append(labeled_results[i]['results']['D27']['answer_label'])
            D28.append(labeled_results[i]['results']['D28']['answer_label'])
            D29.append(labeled_results[i]['results']['D29']['answer_label'])
            D30.append(labeled_results[i]['results']['D30']['answer_label'])
            D31.append(labeled_results[i]['results']['D31']['answer_label'])
            D32.append(labeled_results[i]['results']['D32']['answer_label'])
            D33.append(labeled_results[i]['results']['D33']['answer_label'])
            D34.append(labeled_results[i]['results']['D34']['answer_label'])
            D35.append(labeled_results[i]['results']['D35']['answer_label'])
            D36.append(labeled_results[i]['results']['D36']['answer_label'])
            D37.append(labeled_results[i]['results']['D37']['answer_label'])
            D38.append(labeled_results[i]['results']['D38']['answer_label'])
            D39.append(labeled_results[i]['results']['D39']['answer_label'])
            D40.append(labeled_results[i]['results']['D40']['answer_label'])
            D41.append(labeled_results[i]['results']['D41']['answer_label'])
            D42.append(labeled_results[i]['results']['D42']['answer_label'])
            D43.append(labeled_results[i]['results']['D43']['answer_label'])
            E1.append(labeled_results[i]['results']['E1']['answer_label'])
            E2.append(labeled_results[i]['results']['E2']['answer_label'])
            E3.append(labeled_results[i]['results']['E3']['answer_label'])
            E4.append(labeled_results[i]['results']['E4']['answer_label'])
            if(labeled_results[i]['results']['E4']['answer_label']=="Non"):
                E5.append("NA")
                E6.append("NA")
                E7.append("NA")
                E8.append("NA")
                E9.append("NA")
                E10.append("NA")
                E11.append("NA")
                E12.append("NA")
                E13.append("NA")

            else:
                E5.append(labeled_results[i]['results']['E5']['answer_label'])
                E6.append(labeled_results[i]['results']['E6']['answer_label'])
                E7.append(labeled_results[i]['results']['E7']['answer_label'])
                E8.append(labeled_results[i]['results']['E8']['answer_label'])
                E9.append(labeled_results[i]['results']['E9']['answer_label'])
                E10.append(labeled_results[i]['results']['E10']['answer_label'])
                E11.append(labeled_results[i]['results']['E11']['answer_label'])
                E12.append(labeled_results[i]['results']['E12']['answer_label'])
                E13.append(labeled_results[i]['results']['E13']['answer_label'])
            E13_001.append(labeled_results[i]['results']['E13_001']['answer_label'])
            E13_002.append(labeled_results[i]['results']['E13_002']['answer_label'])
            E14.append(labeled_results[i]['results']['E14']['answer_label'].strip())
            E15.append(labeled_results[i]['results']['E15']['answer_label'])
            if(labeled_results[i]['results']['E15']['answer_label']=="Non"):
                E16.append("NaN")
            else:
                E16.append(labeled_results[i]['results']['E16']['answer_label'].strip())
                print(E18)
            try:
                E18.append(labeled_results[i]['results']['E18']['answer_label'].strip())

            except:
                E18.append("NaN")
                print("cette question n'existe pas ")
    
            HF.append(labeled_results[i]['results']['HF']['answer_label'].strip())


                


    




   




    #C6.append(labeled_results[i]['results']['C6']['answer_label'].strip())

                   
        data={
                labeled_results[0]['results']['No']['label'][0:-2]:N0,
                labeled_results[0]['results']['A1']['label'][0:-2]:A1,
                labeled_results[0]['results']['A2']['label'][0:-2]:A2,
                labeled_results[0]['results']['A3']['label'][0:-2]:A3,
                labeled_results[0]['results']['A4']['label'][0:-2]:A4,
                labeled_results[0]['results']['A5']['label'][0:-2]:A5,
                labeled_results[0]['results']['A6']['label'][0:-2]:A6,
            ######section 2#############################################""
                labeled_results[0]['results']['Bo']['label'][0:-2]:Bo,
                labeled_results[0]['results']['Bo1']['label'][0:-2]:Bo1,
                labeled_results[0]['results']['B1']['label'][0:34].strip():B1,
                labeled_results[0]['results']['B2']['label'][0:49].strip():B2,
                labeled_results[0]['results']['B3']['label'][0:-2]:B3,
                labeled_results[0]['results']['B4']['label'][0:-2]:B4,
                labeled_results[0]['results']['B4_001']['label'][0:-2]: B4_001,
                labeled_results[0]['results']['B5']['label'][0:-2]:B5,
                labeled_results[0]['results']['B6']['label'][0:-2]:B6,
                labeled_results[0]['results']['B8']['label'][0:-2]:B8,
                labeled_results[0]['results']['B10']['label'][0:-2]:B10,
            #####SECTION3 : IDENTIFICATION DES MEMBRES DU BUREAU DE LA FEDERATION OU DU GROUPEMENT SPORTIF
                labeled_results[0]['results']['C1']['label'][0:-2]:C1,
                labeled_results[0]['results']['C2']['label'][0:-2]:C2,
                labeled_results[0]['results']['C3']['label'][0:-2]:C3,
                labeled_results[0]['results']['C5']['label'][0:-2]:C5,
                labeled_results[0]['results']['C6']['label'][0:-2]: C6,
                labeled_results[0]['results']['C7']['label'][0:-2]:C7,
                labeled_results[0]['results']['C8']['label'][0:-2]:C8,
                labeled_results[0]['results']['C9']['label'][0:-2]:C9,
                labeled_results[0]['results']['C10']['label'][0:-2].strip():C10,
            ############################SECTION 4 : COMPOSITION ET SITUATION DES FEDERATIONS ET REGROUPEMENTS SPORTIFS
                labeled_results[0]['results']['D1']['label'][0:-2]:D1,
                labeled_results[0]['results']['D2']['label'][0:-2].strip():D2,
                labeled_results[0]['results']['D3']['label'][0:-2]:D3,
                labeled_results[0]['results']['D4']['label'][0:-2]:D4,
                labeled_results[0]['results']['D5']['label'][2:-2]:D5,
                labeled_results[0]['results']['D5_001']['label']:D5_001,
                labeled_results[0]['results']['D5_002']['label']:D3,
                labeled_results[0]['results']['D6']['label'][0:-2].strip():D6,
                labeled_results[0]['results']['D6_001']['label'][0:-2]:D6_001,
                labeled_results[0]['results']['D6_002']['label']:D6_002,
                labeled_results[0]['results']['D7_003']['label']:D7_003,
                labeled_results[0]['results']['D7_004']['label'][0:-2]:D7_004,
                labeled_results[0]['results']['D7_005']['label'][0:-1]:D7_005,
                labeled_results[0]['results']['D7_006']['label'][0:-2]:D7_006,
                labeled_results[0]['results']['D8']['label'][0:-1]:D8,
                labeled_results[0]['results']['D9']['label'][0:-2].strip():D9,
                labeled_results[0]['results']['D10']['label'][0:-2]:D10,
                labeled_results[0]['results']['D11']['label'][0:-2]:D11,
                labeled_results[0]['results']['D12']['label'][0:-4]:D12,
                labeled_results[0]['results']['D15']['label'][0:-3].strip():D15,
                labeled_results[0]['results']['D16']['label'][0:-2].strip():D16,
                labeled_results[0]['results']['D17']['label'][0:-2]:D17,
                labeled_results[0]['results']['D18']['label'][2:-2]:D18,
                labeled_results[0]['results']['D18_001']['label']:D18_001,
                labeled_results[0]['results']['D19']['label'][0:-2]:D19,
                labeled_results[0]['results']['D20']['label'][0:27]:D20,
                labeled_results[0]['results']['D21']['label'][0:67].strip():D21,
                labeled_results[0]['results']['D22']['label'][0:37]:D22,
                labeled_results[0]['results']['D23']['label'][0:-2].strip():D23,
                labeled_results[0]['results']['D24']['label'][0:57].strip():D24,
                labeled_results[0]['results']['D25']['label'][0:-2].strip():D25,
                labeled_results[0]['results']['D26']['label'][0:-2].strip():D26,
                labeled_results[0]['results']['D27']['label'][0:-2].strip():D27,
                labeled_results[0]['results']['D28']['label'][0:-2].strip():D28,
                labeled_results[0]['results']['D29']['label'][0:-2].strip():D29,
                labeled_results[0]['results']['D30']['label'][0:-2].strip():D30,
                labeled_results[0]['results']['D31']['label'][0:-2].strip():D31,
                labeled_results[0]['results']['D32']['label'][0:-2].strip():D32,
                labeled_results[0]['results']['D33']['label'][0:-2].strip():D33,
                labeled_results[0]['results']['D34']['label'][0:48].strip():D34,
                labeled_results[0]['results']['D35']['label'][0:-2].strip():D35,
                labeled_results[0]['results']['D36']['label'][0:-2].strip():D36,
                labeled_results[0]['results']['D37']['label'][0:57].strip():D37,
                labeled_results[0]['results']['D38']['label'][0:95].strip():D38,
                labeled_results[0]['results']['D39']['label'][0:44].strip():D39,
                labeled_results[0]['results']['D40']['label'][0:44].strip():D40,
                labeled_results[0]['results']['D41']['label'][0:42].strip():D41,
                labeled_results[0]['results']['D42']['label'][0:45].strip():D42,
                labeled_results[0]['results']['D43']['label'][0:53].strip():D43,
                labeled_results[0]['results']['E1']['label'][0:-2].strip():E1,
                labeled_results[0]['results']['E2']['label'][0:-2].strip():E2,
                labeled_results[0]['results']['E3']['label'][0:-2].strip():E3,
                labeled_results[0]['results']['E4']['label'][0:-2].strip():E4,
                labeled_results[0]['results']['E5']['label'][0:-2].strip():E5,
                labeled_results[0]['results']['E6']['label'][0:-2].strip():E6,   
                labeled_results[0]['results']['E7']['label'][0:-3].strip():E7,   
                labeled_results[0]['results']['E8']['label'][0:-2].strip():E8,   
                labeled_results[0]['results']['E9']['label'][0:-2].strip():E9,   
                labeled_results[0]['results']['E10']['label'][0:-2].strip():E10,   
                labeled_results[0]['results']['E11']['label'][0:-2].strip():E11,   
                labeled_results[0]['results']['E12']['label'][0:-2].strip():E12,   
                labeled_results[0]['results']['E13']['label'][0:-2].strip():E13,
                labeled_results[0]['results']['E13_001']['label'][0:-1].strip():E13_001,
                labeled_results[0]['results']['E13_002']['label'][0:-1].strip():E13_002,
                labeled_results[0]['results']['E14']['label'][0:-2].strip():E14,
                labeled_results[0]['results']['E15']['label'][0:-3].strip():E15,
                labeled_results[0]['results']['E16']['label'][0:-2].strip():E16,
                labeled_results[0]['results']['E18']['label'][0:-2].strip():E18,
                labeled_results[0]['results']['HF']['label'][0:-2].strip():HF,}
        return pd.DataFrame(data)



        



        

kobdata=GetKoboData()
labeld_results=kobdata.getAllData()
print(labeld_results)
data=kobdata.getDapsDataFrame(labeld_results)
print(data.head())
#print(data.columns)