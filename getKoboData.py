import pandas as pd
import re 
from koboextractor import KoboExtractor

class GetKoboData:

    def __init__(self):
        self.KOBO_TOKEN="195930fa6955af494ccd95acc9d8e5e8e51e2796"
        self.kobo = KoboExtractor(self.KOBO_TOKEN, 'https://kobo.humanitarianresponse.info/api/v2', debug=True)


    def getAllData(self):
        assets = self.kobo.list_assets()
        asset_uid = assets['results'][0]['uid']
        asset = self.kobo.get_asset(asset_uid)
        choice_lists = self.kobo.get_choices(asset)
        questions = self.kobo.get_questions(asset=asset, unpack_multiples=True)
        asset_data = self.kobo.get_data(asset_uid)
        results = self.kobo.sort_results_by_time(asset_data['results'])
        labeled_results = []
        for result in results:
            labeled_results.append(self.kobo.label_result(unlabeled_result=result, choice_lists=choice_lists, questions=questions, unpack_multiples=True))
            
        return labeled_results


    def getDapsDataFrame(self,labeled_results):

        question_num=[]
        code_enqueteur=[]
        prenom_enqueteur=[]
        nom_enqueteur=[]
        tel_enqueteur=[]
        date_interview=[]
        heure_debut=[]
        nom_structure=[]
        date_creation=[]
        siege_structure=[]
        statut_structure=[]
        discipline_structure=[]
        outil_structure=[]
        locaux_structure=[]
        statut_occpation_structure=[]
        sexe_membre=[]
        profession_membre=[]
        formation_membre=[]
        profil_membre=[]
        diplome_membre=[]
        experience_sport_membre=[]
        tete_oraganisation_membre=[]
        durée_mandat_membre=[]
        montant_budget_annuel=[]
        commite_directeur=[]
        nombre_femme=[]
        D3=[]
        D4=[]
        D5=[]
        D6=[]
        D7=[]
        D8=[]
        D9=[]
        D10=[]
        D11=[]
        D12=[]
        D13=[]
        D14=[]
        D15=[]
        D16=[]
        D17=[]
        D18=[]
        D19=[]
        D20=[]
        D21=[]
        D22=[]
        D23=[]
        D24=[]
        D25=[]
        D26=[]
        D27=[]
        D28=[]
        D29=[]
        D30=[]
        D31=[]
        D32=[]
        D33=[]
        D34=[]
        D35=[]
        D36=[]
        D37=[]
        D38=[]
        D39=[]
        D40=[]
        D41=[]
        D42=[]
        D43=[]
        ################E#########
        E1=[]
        E2=[]
        E3=[]
        E4=[]
        E5=[]
        E6=[]
        E7=[]
        E8=[]
        E9=[]
        E10=[]
        E11=[]
        E12=[]
        E13=[]
        E14=[]
        E15=[]
        E16=[]
        #E17=[]
        E18=[]
        # E19=[]
        # E20=[]
        # E21=[]
        # E22=[]

        for i in range(0,len(labeled_results)):
            for label in labeled_results[i]['results']['No']['answer_label']:
                question_num.append(label)
                ##k' index à changer
            for label in labeled_results[1]['results']['A1']['answer_label']:
                code_enqueteur.append(label)
                prenom_enqueteur.append(labeled_results[i]['results']['A2']['answer_label'])
                nom_enqueteur.append(labeled_results[i]['results']['A3']['answer_label'])
                tel_enqueteur.append(labeled_results[i]['results']['A4']['answer_label'])
                date_interview.append(labeled_results[i]['results']['A5']['answer_label'])
                heure_debut.append(labeled_results[i]['results']['A6']['answer_label'])
                nom_structure.append(labeled_results[i]['results']['B1']['answer_label'])
                date_creation.append(labeled_results[i]['results']['B2']['answer_label'])
                siege_structure.append(labeled_results[i]['results']['B3']['answer_label'])
                statut_structure.append(labeled_results[i]['results']['B4']['answer_label'][0:-1])
                discipline_structure.append(labeled_results[i]['results']['B5']['answer_label'][0:-1])
                outil_structure.append(labeled_results[i]['results']['B6']['answer_label'][0:-1])
                locaux_structure.append(labeled_results[i]['results']['B8']['answer_label'])
                statut_occpation_structure.append(labeled_results[i]['results']['B9']['answer_label'])
                sexe_membre.append(labeled_results[i]['results']['C1']['answer_label'])
                profession_membre.append(labeled_results[i]['results']['C2']['answer_label'])
                diplome_membre.append(labeled_results[i]['results']['C3']['answer_label'][0:-1])
                formation_membre.append(labeled_results[i]['results']['C5']['answer_label'][0:-1])
                profil_membre.append(labeled_results[i]['results']['C6']['answer_label'][0:-1])
                experience_sport_membre.append(labeled_results[i]['results']['C7']['answer_label'][0:-1])
                tete_oraganisation_membre.append(labeled_results[i]['results']['C8']['answer_label'][0:-1])
                durée_mandat_membre.append(labeled_results[i]['results']['C9']['answer_label'][0:-1])
                montant_budget_annuel.append(labeled_results[i]['results']['C10']['answer_label'][0:-1])
                commite_directeur.append(labeled_results[i]['results']['D1']['answer_label'][0:-1])
                nombre_femme.append(labeled_results[i]['results']['D2']['answer_label'][0:-1])
                D3.append(labeled_results[i]['results']['D3']['answer_label'][0:-1])
                D4.append(labeled_results[i]['results']['D4']['answer_label'][0:-1])
                D5.append(labeled_results[i]['results']['D5']['answer_label'][0:-1])
                D6.append(labeled_results[i]['results']['D6']['answer_label'][0:-1])
                D7.append(labeled_results[i]['results']['D7']['answer_label'][0:-1])
                D8.append(labeled_results[i]['results']['D8']['answer_label'][0:-1])
                D9.append(labeled_results[i]['results']['D9']['answer_label'][0:-1])
                D10.append(labeled_results[i]['results']['D10']['answer_label'][0:-1])
                D11.append(labeled_results[i]['results']['D11']['answer_label'][0:-1])
                D12.append(labeled_results[i]['results']['D12']['answer_label'][0:-1])
                D13.append(labeled_results[i]['results']['D13']['answer_label'][0:-1])
                D14.append(labeled_results[i]['results']['D14']['answer_label'][0:-1])
                D15.append(labeled_results[i]['results']['D15']['answer_label'][0:-1])
                D16.append(labeled_results[i]['results']['D16']['answer_label'][0:-1])
                D17.append(labeled_results[i]['results']['D17']['answer_label'][0:-1])
                D18.append(labeled_results[i]['results']['D18']['answer_label'][0:-1])
                D19.append(labeled_results[i]['results']['D19']['answer_label'][0:-1])
                D20.append(labeled_results[i]['results']['D20']['answer_label'][0:-1])
                D21.append(labeled_results[i]['results']['D21']['answer_label'][0:-1])
                D22.append(labeled_results[i]['results']['D22']['answer_label'][0:-1])
                D23.append(labeled_results[i]['results']['D23']['answer_label'][0:-1])
                D24.append(labeled_results[i]['results']['D24']['answer_label'][0:-1])
                D25.append(labeled_results[i]['results']['D25']['answer_label'][0:-1])
                D26.append(labeled_results[i]['results']['D26']['answer_label'][0:-1])
                D27.append(labeled_results[i]['results']['D27']['answer_label'][0:-1])
                D28.append(labeled_results[i]['results']['D28']['answer_label'][0:-1])
                D29.append(labeled_results[i]['results']['D29']['answer_label'][0:-1])
                D30.append(labeled_results[i]['results']['D30']['answer_label'][0:-1])
                D31.append(labeled_results[i]['results']['D31']['answer_label'][0:-1])
                D32.append(labeled_results[i]['results']['D32']['answer_label'][0:-1])
                D33.append(labeled_results[i]['results']['D33']['answer_label'][0:-1])
                D34.append(labeled_results[i]['results']['D34']['answer_label'][0:-1])
                D35.append(labeled_results[i]['results']['D35']['answer_label'][0:-1])
                D36.append(labeled_results[i]['results']['D36']['answer_label'][0:-1])
                D37.append(labeled_results[i]['results']['D37']['answer_label'][0:-1])
                D38.append(labeled_results[i]['results']['D38']['answer_label'][0:-1])
                D39.append(labeled_results[i]['results']['D39']['answer_label'][0:-1])
                D40.append(labeled_results[i]['results']['D40']['answer_label'][0:-1])
                D41.append(labeled_results[i]['results']['D41']['answer_label'][0:-1])
                D42.append(labeled_results[i]['results']['D42']['answer_label'][0:-1])
                D43.append(labeled_results[i]['results']['D43']['answer_label'][0:-1])
                #################EEEEE#########################################
                E1.append(labeled_results[i]['results']['E1']['answer_label'][0:-1])
                E2.append(labeled_results[i]['results']['E2']['answer_label'][0:-1])
                E3.append(labeled_results[i]['results']['E3']['answer_label'][0:-1])
                E4.append(labeled_results[i]['results']['E4']['answer_label'][0:-1])
                E5.append(labeled_results[i]['results']['E5']['answer_label'][0:-1])
                E6.append(labeled_results[i]['results']['E6']['answer_label'][0:-1])
                E7.append(labeled_results[i]['results']['E7']['answer_label'][0:-1])
                E8.append(labeled_results[i]['results']['E8']['answer_label'][0:-1])
                E9.append(labeled_results[i]['results']['E9']['answer_label'][0:-1])
                E10.append(labeled_results[i]['results']['E10']['answer_label'][0:-1])
                E11.append(labeled_results[i]['results']['E11']['answer_label'][0:-1])
                E12.append(labeled_results[i]['results']['E12']['answer_label'][0:-1])
                E13.append(labeled_results[i]['results']['E13']['answer_label'][0:-1])
                E14.append(labeled_results[i]['results']['E14']['answer_label'][0:-1])
                E15.append(labeled_results[i]['results']['E15']['answer_label'][0:-1])
                E16.append(labeled_results[i]['results']['E16']['answer_label'][0:-1])
                #E17.append(labeled_results[i]['results']['E17']['answer_label'])
                E18.append(labeled_results[i]['results']['E18']['answer_label'][0:-1])
        #         E19.append(labeled_results[i]['results']['E19']['answer_label'])
        #         E20.append(labeled_results[i]['results']['E20']['answer_label'])
        #         E21.append(labeled_results[i]['results']['E21']['answer_label'])
        #         E22.append(labeled_results[i]['results']['E22']['answer_label'])

            
            print(i)
            
            data={
                labeled_results[0]['results']['No']['label'][0:-3]:question_num, 
                labeled_results[1]['results']['A1']['label'][0:-2]:code_enqueteur,
                labeled_results[1]['results']['A2']['label'][0:-2]:prenom_enqueteur,
                labeled_results[1]['results']['A3']['label'][0:-2]:nom_enqueteur,
                labeled_results[1]['results']['A4']['label'][0:-2]:tel_enqueteur,
                labeled_results[1]['results']['A5']['label'][0:-2]: date_interview,
                labeled_results[1]['results']['A6']['label'][0:-2]: heure_debut,
                labeled_results[1]['results']['B1']['label'][0:-6]: nom_structure,
                labeled_results[1]['results']['B2']['label'][0:-4]: date_creation,
                labeled_results[1]['results']['B3']['label'][0:-4] :siege_structure,
                labeled_results[1]['results']['B4']['label'][0:-4] :statut_structure,
                labeled_results[1]['results']['B5']['label'][0:-4] :discipline_structure,
                labeled_results[1]['results']['B6']['label'][0:-4] :outil_structure,
                labeled_results[1]['results']['B8']['label'][0:-2]:locaux_structure,
                labeled_results[1]['results']['B9']['label'][0:-2]:statut_occpation_structure,
                labeled_results[1]['results']['C1']['label'][0:-2]:sexe_membre,
                labeled_results[1]['results']['C2']['label'][0:-2]:profession_membre,
                labeled_results[1]['results']['C3']['label'][0:-1]:diplome_membre,
                labeled_results[1]['results']['C5']['label'][0:-1]:formation_membre,
                labeled_results[1]['results']['C6']['label'][0:-1]:profil_membre,
                labeled_results[1]['results']['C7']['label'][0:-1]:experience_sport_membre,
                labeled_results[1]['results']['C8']['label'][0:-1]:tete_oraganisation_membre,
                labeled_results[1]['results']['C9']['label'][0:-1]:durée_mandat_membre,
                labeled_results[1]['results']['C10']['label'][0:-1]:montant_budget_annuel,
                labeled_results[1]['results']['D1']['label'][0:-1]:commite_directeur,
                labeled_results[1]['results']['D2']['label'][0:-1]:nombre_femme,
                labeled_results[1]['results']['D3']['label'][0:-1]:D3,
                labeled_results[1]['results']['D4']['label'][0:-1]:D4,
                labeled_results[1]['results']['D5']['label'][0:-1]:D5,
                labeled_results[1]['results']['D6']['label'][0:-1]:D6,
                labeled_results[1]['results']['D7']['label'][0:-1]:D7,
                labeled_results[1]['results']['D8']['label'][0:-1]:D8,
                labeled_results[1]['results']['D9']['label'][0:-1]:D9,
                labeled_results[1]['results']['D10']['label'][0:-1]:D10,
                labeled_results[1]['results']['D11']['label'][0:-1]:D11,
                labeled_results[1]['results']['D12']['label'][0:-1]:D12,
                labeled_results[1]['results']['D13']['label'][0:-1]:D13,
                labeled_results[1]['results']['D14']['label'][0:-1]:D14,
                labeled_results[1]['results']['D15']['label'][0:-1]:D15,
                labeled_results[1]['results']['D16']['label'][0:-1]:D16,
                labeled_results[1]['results']['D17']['label'][0:-1]:D17,
                labeled_results[1]['results']['D18']['label'][0:-1]:D18,
                labeled_results[1]['results']['D19']['label'][0:-1]:D19,
                labeled_results[1]['results']['D20']['label'][0:-1]:D20,
                labeled_results[1]['results']['D21']['label'][0:-1]:D21,
                labeled_results[1]['results']['D22']['label'][0:-1]:D22,
                labeled_results[1]['results']['D23']['label'][0:-1]:D23,
                labeled_results[1]['results']['D24']['label'][0:-1]:D24,
                labeled_results[1]['results']['D25']['label'][0:-1]:D25,
                labeled_results[1]['results']['D26']['label'][0:-1]:D26,
                labeled_results[1]['results']['D27']['label'][0:-1]:D27,
                labeled_results[1]['results']['D28']['label'][0:-1]:D28,
                labeled_results[1]['results']['D29']['label'][0:-1]:D29,
                labeled_results[1]['results']['D30']['label'][0:-1]:D30,
                labeled_results[1]['results']['D31']['label'][0:-1]:D31,
                labeled_results[1]['results']['D32']['label'][0:-1]:D32,
                labeled_results[1]['results']['D33']['label'][0:-1]:D33,
                labeled_results[1]['results']['D34']['label'][0:-1]:D34,
                labeled_results[1]['results']['D35']['label'][0:-1]:D35,
                labeled_results[1]['results']['D36']['label'][0:-1]:D36,
                labeled_results[1]['results']['D37']['label'][0:-1]:D37,
                labeled_results[1]['results']['D38']['label'][0:-1]:D38,
                labeled_results[1]['results']['D39']['label'][0:-1]:D39,
                labeled_results[1]['results']['D40']['label'][0:-1]:D40,
                labeled_results[1]['results']['D41']['label'][0:-1]:D41,
                labeled_results[1]['results']['D42']['label'][0:-1]:D42,
                labeled_results[1]['results']['D43']['label'][0:-1]:D43,
                ###EEEEEEEEEEEEEEEEEEEEEEEEEEE########################
                labeled_results[1]['results']['E1']['label'][0:-1]:E1,
                labeled_results[1]['results']['E2']['label'][0:-1]:E2,
                labeled_results[1]['results']['E3']['label'][0:-1]:E3,
                labeled_results[1]['results']['E4']['label'][0:-1]:E4,
                labeled_results[1]['results']['E5']['label'][0:-1]:E5,
                labeled_results[1]['results']['E6']['label'][0:-1]:E6,
                labeled_results[1]['results']['E7']['label'][0:-1]:E7,
                labeled_results[1]['results']['E8']['label'][0:-1]:E8,
                labeled_results[1]['results']['E9']['label'][0:-1]:E9,
                labeled_results[1]['results']['E10']['label'][0:-1]:E10,
                labeled_results[1]['results']['E11']['label'][0:-1]:E11,
                labeled_results[1]['results']['E12']['label'][0:-1]:E12,
                labeled_results[1]['results']['E13']['label'][0:-1]:E13,
                labeled_results[1]['results']['E14']['label'][0:-1]:E14,
                labeled_results[1]['results']['E15']['label'][0:-1]:E15,
                labeled_results[1]['results']['E16']['label'][0:-1]:E16,
                labeled_results[1]['results']['E18']['label'][0:-1]:E18
                 
            }
        return pd.DataFrame(data)


kobdata=GetKoboData()
labeld_results=kobdata.getAllData()
data=kobdata.getDapsDataFrame(labeld_results)
print(data)
print(data.columns)