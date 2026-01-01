"""

Link de todas as apis do Sidra IBGE
Fonte: https://sidra.ibge.gov.br/
"""

APIS = {
    'abate_1092': {
         'url': 'https://apisidra.ibge.gov.br/values/t/1092/n1/all/n3/all/v/all/p/first%201/c12716/all/c18/all/c12529/all/d/v1000151%202,v1000284%202,v1000285%202',
         'period': 'quarterly'
    },
    'abate_1093': {
          'url': 'https://apisidra.ibge.gov.br/values/t/1093/n1/all/n3/all/v/all/p/first%201/c12716/all/c12529/all/d/v1000151%202,v1000284%202,v1000285%202',
          'period': 'quarterly'
    },
    'abate_1094': {
          'url': 'https://apisidra.ibge.gov.br/values/t/1094/n1/all/n3/all/v/all/p/first%201/c12716/all/c12529/all/d/v1000151%202,v1000284%202,v1000285%202',
          'period': 'quarterly'
    },
     'leite_1086': {
         'url': 'https://apisidra.ibge.gov.br/values/t/1086/n1/all/n3/all/v/all/p/first%201/c12716/all/c12529/all/d/v282%200,v283%200,v2522%202,v1000151%202,v1000282%202,v1000283%202',
         'period': 'quarterly'
    },
     'couro_1088': {
         'url': 'https://apisidra.ibge.gov.br/values/t/1088/n1/all/n3/all/v/all/p/first%201/c12716/all/c11531/all/d/v1000151%202,v1000622%202',
         'period': 'quarterly'
    },
     'couro_1089': {
         'url': 'https://apisidra.ibge.gov.br/values/t/1089/n1/all/n3/all/v/all/p/first%201/c12716/all/d/v1000151%202,v1000623%202,v1002417%202',
         'period': 'quarterly'
    },
     'couro_1090': {
         'url': 'https://apisidra.ibge.gov.br/values/t/1090/n1/all/n3/all/v/all/p/first%201/c12716/all/c11532/all/d/v1000151%202,v1000624%202',
         'period': 'quarterly'
    },
     'ovo_7524': {
         'url': 'https://apisidra.ibge.gov.br/values/t/7524/n1/all/n3/all/v/all/p/first%201/c12716/all/c1835/all/d/v1000029%202',
         'period': 'quarterly'
    },
     'producao_agricola_188': {
         'url': 'https://apisidra.ibge.gov.br/values/t/188/n1/all/n2/all/n3/all/v/all/p/all/c49/all/c48/all',
         'period': 'one-month'
    },
     'producao_agricola_1618': {
         'url': 'https://apisidra.ibge.gov.br/values/t/1618/n1/all/n2/all/n3/all/v/all/p/all/c49/all/c48/all',
         'period': 'one-month'
    },
      'producao_agricola_6588': {
           'url': 'https://apisidra.ibge.gov.br/values/t/6588/n1/all/n2/all/n3/all/v/all/p/first%201/c48/all',
           'period': 'monthly'
    },
      'producao_agricola_7832': {
          'url': 'https://apisidra.ibge.gov.br/values/t/7832/n1/all/n2/all/n3/all/v/all/p/all/c49/all/c48/all',
          'period': 'one-month'
    },
     'producao_agricola_7878': {
          'url': 'https://apisidra.ibge.gov.br/values/t/7878/n1/all/n2/all/n3/all/v/all/p/first%201/c48/all',
          'period': 'monthly'
    },
       'estoque_254': {
           'url': 'https://apisidra.ibge.gov.br/values/t/254/n1/all/n2/all/v/all/p/first%201/c162/all/c161/all/c163/all/d/v1000150%202,v1000151%202',
           'period': 'semester'
    },
	  'estoque_255': {
          'url': 'https://apisidra.ibge.gov.br/values/t/255/n1/all/n2/all/v/all/p/first%201/c162/all',
          'period': 'semester'
      },
	  'estoque_259': {
          'url': 'https://apisidra.ibge.gov.br/values/t/259/n1/all/n2/all/v/all/p/first%201/c12687/all/d/v1000151%202,v1000153%202',
          'period': 'semester'
      },
	  'estoque_278': {
          'url': 'https://apisidra.ibge.gov.br/values/t/278/n1/all/n2/all/v/all/p/first%201/c166/all/c161/all/c163/all',
          'period': 'semester'
      },
	  'estoque_911': {
          'url': 'https://apisidra.ibge.gov.br/values/t/911/n1/all/n2/all/v/all/p/first%201/c166/all',
          'period': 'semester'
      },
	  'estoque_912': {
          'url': 'https://apisidra.ibge.gov.br/values/t/912/n1/all/n2/all/v/all/p/first%201',
          'period': 'semester'
      },
	  'estoque_5459': {
          'url': 'https://apisidra.ibge.gov.br/values/t/5470/n1/all/n2/all/v/all/p/first%201/c11278/all/d/v1002171%202,v1002172%202',
          'period': 'semester'
      },
	  'estoque_5470': {
          'url': 'https://apisidra.ibge.gov.br/values/t/5470/n1/all/n2/all/n3/all/v/all/p/first%201/c11278/all/d/v1002171%202,v1002172%202',
          'period': 'semester'
      },
     'ipca_118': {
         'url': 'https://apisidra.ibge.gov.br/values/t/118/n1/all/v/all/p/first%201/d/v306%202',
         'period': 'monthly'
     },
     'ipca_1737': {
         'url': 'https://apisidra.ibge.gov.br/values/t/1737/n1/all/v/all/p/first%201/d/v63%202,v69%202,v2263%202,v2264%202,v2265%202,v2266%2013',
         'period': 'monthly'
     },
     'ipca_6691': {
         'url': 'https://apisidra.ibge.gov.br/values/t/6691/n1/all/v/all/p/first%201/d/v63%202,v2266%2013,v9798%202,v9800%202',
         'period': 'monthly'
     },
     'ipca_7060': {
         'url': 'https://apisidra.ibge.gov.br/values/t/7060/n1/all/n71/all/n7/all/n6/all/v/all/p/first%201/c315/all/d/v63%202,v66%204,v69%202,v2265%202',
         'period': 'monthly'
     },
     'ipca_7061': {
         'url': 'https://apisidra.ibge.gov.br/values/t/7061/n1/all/n71/all/n7/all/n6/all/v/all/p/first%201/c315/all/d/v306%202,v307%202,v309%204',
         'period': 'monthly'
     },
     'inpc_1736': {
         'url': 'https://apisidra.ibge.gov.br/values/t/1736/n1/all/v/all/p/first%201/d/v44%202,v68%202,v2289%2013,v2290%202,v2291%202,v2292%202',
         'period': 'monthly'
     },
     'inpc_7063': {
         'url': 'https://apisidra.ibge.gov.br/values/t/7063/n1/all/n71/all/n7/all/n6/all/v/all/p/first%201/c315/all/d/v44%202,v45%204,v68%202,v2292%202',
         'period': 'monthly'
     },
    
    # IPCA 15
     'ipca_15_3065': {
         'url': 'https://apisidra.ibge.gov.br/values/t/3065/n1/all/v/all/p/first%201/d/v355%202,v356%202,v1117%2013,v1118%202,v1119%202,v1120%202',
         'period': 'monthly'
     },
     'ipca_15_7062': {
         'url': 'https://apisidra.ibge.gov.br/values/t/7062/n1/all/n71/all/n7/all/n6/all/v/all/p/first%201/c315/all/d/v355%202,v356%202,v357%204,v1120%202',
         'period': 'monthly'
     },
    
     #SINAPI
     'sinapi_647': {
         'url': 'https://apisidra.ibge.gov.br/values/t/647/n3/all/v/all/p/first%201/c314/all/c41/all/d/v51%202',
         'period': 'monthly'
     },
     'sinapi_2296': {
         'url': 'https://apisidra.ibge.gov.br/values/t/2296/n1/all/n2/all/n3/all/v/all/p/first%201/d/v48%202,v49%202,v1193%202,v1196%202,v1197%202,v1198%202,v1232%202,v2119%202,v2120%202',
         'period': 'monthly'
     },
     'sinapi_6586': {
         'url': 'https://apisidra.ibge.gov.br/values/t/6586/n1/all/n2/all/n3/all/v/all/p/first%201/d/v9327%202,v9328%202,v9329%202,v9330%202,v9331%202,v9332%202,v9333%202,v9334%202,v9335%202',
         'period': 'monthly'
     },
    
     #PIMPF/BR
     'pim_pf_br_8885': {
         'url': 'https://apisidra.ibge.gov.br/values/t/8885/n1/all/v/all/p/first%201/c542/all/d/v11602%201,v11603%201,v11604%201,v12606%205',
         'period': 'monthly'
     },
     'pim_pf_br_8886': {
         'url': 'https://apisidra.ibge.gov.br/values/t/8886/n1/all/v/all/p/first%201/d/v11602%201,v11603%201,v11604%201,v12606%205',
         'period': 'monthly'
     },
     'pim_pf_br_8887': {
         'url': 'https://apisidra.ibge.gov.br/values/t/8887/n1/all/v/all/p/first%201/c543/all/d/v11601%201,v11602%201,v11603%201,v11604%201,v12606%205,v12607%205',
         'period': 'monthly'
     },
     'pim_pf_br_8888': {
         'url': 'https://apisidra.ibge.gov.br/values/t/8888/n1/all/n2/all/n3/all/v/all/p/first%201/c544/all/d/v11601%201,v11602%201,v11603%201,v11604%201,v12606%205,v12607%205',
         'period': 'monthly'
     },
     'pim_pf_br_8889': {
         'url': 'https://apisidra.ibge.gov.br/values/t/8889/n1/all/v/all/p/first%201/c25/all/d/v11602%201,v11603%201,v11604%201,v12606%205',
         'period': 'monthly'
     },
    
     #PIMPF/rg'
     'pim_pf_rg_8888': {
         'url': 'https://apisidra.ibge.gov.br/values/t/8888/n1/all/n2/all/n3/all/v/all/p/first%201/c544/all/d/v11601%201,v11602%201,v11603%201,v11604%201,v12606%205,v12607%205',
         'period': 'monthly'
     },
    
     #ipp
     'ipp_6723': {
         'url': 'https://apisidra.ibge.gov.br/values/t/6723/n1/all/v/all/p/first%201/c844/all/d/v1394%202,v1395%202,v1396%202,v10008%205',
         'period': 'monthly'
     },
     'ipp_6903': {
         'url': 'https://apisidra.ibge.gov.br/values/t/6903/n1/all/v/all/p/first%201/c842/all/d/v1394%202,v1395%202,v1396%202,v10008%205',
         'period': 'monthly'
     },
     'ipp_6904': {
         'url': 'https://apisidra.ibge.gov.br/values/t/6904/n1/all/v/all/p/first%201/c543/all/d/v1394%202,v1395%202,v1396%202,v10008%205',
         'period': 'monthly'
     },
    
    #pnadcm - 3 meses
    'pnadcm_3918':{
        'url': 'https://apisidra.ibge.gov.br/values/t/3918/n1/all/v/all/p/first%201/c12027/all/d/v4091%201,v8430%201,v8435%201',
        'period': 'three-month'
    },
    'pnadcm_3919':{
        'url': 'https://apisidra.ibge.gov.br/values/t/3919/n1/all/v/all/p/first%201/d/v8463%201,v8464%201,v8465%201,v8469%201',
        'period': 'three-month'
    },
    'pnadcm_5944':{
        'url': 'https://apisidra.ibge.gov.br/values/t/5944/n1/all/v/all/p/first%201/d/v4096%201,v4100%201,v8778%201,v8783%201',
        'period': 'three-month'
    },
    'pnadcm_6022':{
        'url': 'https://apisidra.ibge.gov.br/values/t/6022/n1/all/v/all/p/first%201/d/v6541%201,v6867%201,v6872%201',
        'period': 'three-month'
    },
    'pnadcm_6318':{
        'url': 'https://apisidra.ibge.gov.br/values/t/6318/n1/all/v/all/p/first%201/c629/all/d/v4087%201,v8399%201,v8404%201',
        'period': 'three-month'
    },
    'pnadcm_6320':{
        'url': 'https://apisidra.ibge.gov.br/values/t/6320/n1/all/v/all/p/first%201/c11913/all/d/v4091%201,v8430%201,v8435%201',
        'period': 'three-month'
    },
    'pnadcm_6323':{
        'url': 'https://apisidra.ibge.gov.br/values/t/6323/n1/all/v/all/p/first%201/c888/all/d/v4091%201,v8430%201,v8435%201',
        'period': 'three-month'
    },
    'pnadcm_6379':{
        'url': 'https://apisidra.ibge.gov.br/values/t/6379/n1/all/v/all/p/first%201/d/v4097%201,v4101%201,v8789%201,v8794%201',
        'period': 'three-month'
    },
    'pnadcm_6380':{
        'url': 'https://apisidra.ibge.gov.br/values/t/6380/n1/all/v/all/p/first%201/d/v4098%201,v4102%201,v8800%201,v8805%201',
        'period': 'three-month'
    },
    'pnadcm_6381':{
        'url': 'https://apisidra.ibge.gov.br/values/t/6381/n1/all/v/all/p/first%201/d/v4099%201,v4103%201,v8811%201,v8816%201',
        'period': 'three-month'
    },
    'pnadcm_6387':{
        'url': 'https://apisidra.ibge.gov.br/values/t/6387/n1/all/v/all/p/first%201/d/v5939%201,v5943%201,v8843%201,v8848%201,v8854%201,v8859%201',
        'period': 'three-month'
    }, 
    'pnadcm_6388':{
        'url': 'https://apisidra.ibge.gov.br/values/t/6388/n1/all/v/all/p/first%201/d/v5942%201,v8876%201,v8881%201',
        'period': 'three-month'
    },
    'pnadcm_6389':{
        'url': 'https://apisidra.ibge.gov.br/values/t/6389/n1/all/v/all/p/first%201/c11913/all/d/v5940%201,v8898%201,v8903%201',
        'period': 'three-month'
    },
    'pnadcm_6390':{
        'url': 'https://apisidra.ibge.gov.br/values/t/6390/n1/all/v/all/p/first%201/d/v5937%201,v5941%201,v8821%201,v8826%201,v8832%201,v8837%201',
        'period': 'three-month'
    }, 
    'pnadcm_6391':{
        'url': 'https://apisidra.ibge.gov.br/values/t/6391/n1/all/v/all/p/first%201/c888/all/d/v5940%201,v8898%201,v8903%201',
        'period': 'three-month'
    },
    'pnadcm_6392':{
        'url': 'https://apisidra.ibge.gov.br/values/t/6392/n1/all/v/all/p/first%201/d/v6289%201,v6294%201,v8909%201,v8914%201,v8920%201,v8925%201',
        'period': 'three-month'
    }, 
    'pnadcm_6393':{
        'url': 'https://apisidra.ibge.gov.br/values/t/6393/n1/all/v/all/p/first%201/d/v6292%201,v6296%201,v8931%201,v8936%201,v8942%201,v8947%201',
        'period': 'three-month'
    },
    'pnadcm_6438':{
        'url': 'https://apisidra.ibge.gov.br/values/t/6438/n1/all/v/all/p/first%201/c604/all/d/v4087%201,v8399%201,v8404%201',
        'period': 'three-month'
    },  
    'pnadcm_6439':{
        'url': 'https://apisidra.ibge.gov.br/values/t/6439/n1/all/v/all/p/first%201/d/v4114%201,v4115%201,v8641%201,v8645%201',
        'period': 'three-month'
    },
    'pnadcm_6440':{
        'url': 'https://apisidra.ibge.gov.br/values/t/6440/n1/all/v/all/p/first%201/d/v4116%201,v4117%201,v8650%201,v8654%201',
        'period': 'three-month'
    },  
    'pnadcm_6441':{
        'url': 'https://apisidra.ibge.gov.br/values/t/6441/n1/all/v/all/p/first%201/d/v4118%201,v4119%201,v8659%201,v8663%201',
        'period': 'three-month'
    }, 
    'pnadcm_6785':{
        'url': 'https://apisidra.ibge.gov.br/values/t/6785/n1/all/v/all/p/first%201/d/v9819%201,v9820%201,v9821%201,v9825%201',
        'period': 'three-month'
    }, 
    'pnadcm_6807':{
        'url': 'https://apisidra.ibge.gov.br/values/t/6807/n1/all/v/all/p/first%201/d/v9869%201,v9870%201,v9871%201,v9875%201',
        'period': 'three-month'
    }, 
    'pnadcm_8501':{
        'url': 'https://apisidra.ibge.gov.br/values/t/8501/n1/all/v/all/p/first%201/c1350/all/d/v4091%201,v8430%201,v8435%201',
        'period': 'three-month'
    },
    'pnadcm_8513': {
        'url': 'https://apisidra.ibge.gov.br/values/t/8513/n1/all/v/all/p/first%201/d/v12466%201,v12467%201,v12468%201,v12470%201',
        'period': 'three-month'
    },
     
     #PNADC/T
     'pnadct_1616': {
         'url': 'https://apisidra.ibge.gov.br/values/t/1616/n1/all/n2/all/n3/all/v/all/p/first%201/c1965/all/d/v4093%201,v4110%201,v4111%201',
         'period': 'quarterly'
     }, 
     'pnadct_4092': {
         'url': 'https://apisidra.ibge.gov.br/values/t/4092/n1/all/n2/all/v/all/p/first%201/c629/all/d/v4087%201,v4104%201,v4105%201',
         'period': 'quarterly'
     },
     'pnadct_4093': {
         'url': 'https://apisidra.ibge.gov.br/values/t/4093/n1/all/n2/all/v/all/p/first%201/c2/all/d/v4087%201,v4089%201,v4091%201,v4093%201,v4095%201,v4096%201,v4097%201,v4098%201,v4099%201,v4100%201,v4101%201,v4102%201,v4103%201,v4104%201,v4105%201,v4106%201,v4107%201,v4108%201,v4109%201,v4110%201,v4111%201,v4112%201,v4113%201,v4724%201,v4726%201,v4774%201,v12466%201,v12467%201',
         'period': 'quarterly'
     },
     'pnadct_4094': {
         'url': 'https://apisidra.ibge.gov.br/values/t/4094/n1/all/n2/all/v/all/p/first%201/c58/all/d/v4087%201,v4089%201,v4091%201,v4093%201,v4095%201,v4096%201,v4097%201,v4098%201,v4099%201,v4100%201,v4101%201,v4102%201,v4103%201,v4104%201,v4105%201,v4106%201,v4107%201,v4108%201,v4109%201,v4110%201,v4111%201,v4112%201,v4113%201,v4724%201,v4726%201,v4774%201,v12466%201,v12467%201',
         'period': 'quarterly'
     },
     'pnadct_4095': {
         'url': 'https://apisidra.ibge.gov.br/values/t/4095/n1/all/n2/all/v/all/p/first%201/c1568/all/d/v4087%201,v4089%201,v4091%201,v4093%201,v4095%201,v4096%201,v4097%201,v4098%201,v4099%201,v4100%201,v4101%201,v4102%201,v4103%201,v4104%201,v4105%201,v4106%201,v4107%201,v4108%201,v4109%201,v4110%201,v4111%201,v4112%201,v4113%201,v4724%201,v4726%201,v4774%201,v12466%201,v12467%201',
         'period': 'quarterly'
     },
     'pnadct_4096': {
         'url': 'https://apisidra.ibge.gov.br/values/t/4096/n1/all/n2/all/v/all/p/first%201/c12029/all/d/v4091%201,v4108%201,v4109%201',
         'period': 'quarterly'
     },
     'pnadct_4097': {
         'url': 'https://apisidra.ibge.gov.br/values/t/4097/n1/all/n2/all/v/all/p/first%201/c11913/all/d/v4091%201,v4108%201,v4109%201',
         'period': 'quarterly'
     },
     'pnadct_4099': {
         'url': 'https://apisidra.ibge.gov.br/values/t/4099/n1/all/n2/all/v/all/p/first%201/d/v4099%201,v4103%201,v4114%201,v4115%201,v4116%201,v4117%201,v4118%201,v4119%201',
         'period': 'quarterly'
     },
     'pnadct_4100': {
         'url': 'https://apisidra.ibge.gov.br/values/t/4100/n1/all/n2/all/v/all/p/first%201/c604/all/d/v4087%201,v4104%201,v4105%201',
         'period': 'quarterly'
     },
     'pnadct_5434': {
         'url': 'https://apisidra.ibge.gov.br/values/t/5434/n1/all/n2/all/v/all/p/first%201/c888/all/d/v4091%201,v4108%201,v4109%201',
         'period': 'quarterly'
     },
     'pnadct_5435': {
         'url': 'https://apisidra.ibge.gov.br/values/t/5435/n1/all/n2/all/v/all/p/first%201/c694/all/d/v4091%201,v4108%201,v4109%201',
         'period': 'quarterly'
     },
     'pnadct_5436': {
         'url': 'https://apisidra.ibge.gov.br/values/t/5436/n1/all/n2/all/v/all/p/first%201/c2/all/d/v5940%201,v5941%201,v5942%201,v5943%201',
         'period': 'quarterly'
     },
     'pnadct_5437': {
         'url': 'https://apisidra.ibge.gov.br/values/t/5437/n1/all/n2/all/v/all/p/first%201/c58/all/d/v5940%201,v5941%201,v5942%201,v5943%201',
         'period': 'quarterly'
     },
     'pnadct_5438': {
         'url': 'https://apisidra.ibge.gov.br/values/t/5438/n1/all/n2/all/v/all/p/first%201/c1568/all/d/v5940%201,v5941%201,v5942%201,v5943%201',
         'period': 'quarterly'
     },
     'pnadct_5439': {
         'url': 'https://apisidra.ibge.gov.br/values/t/5439/n1/all/n2/all/v/all/p/first%201/c12029/all/d/v5940%201,v5942%201',
         'period': 'quarterly'
     },
     'pnadct_5440': {
         'url': 'https://apisidra.ibge.gov.br/values/t/5440/n1/all/n2/all/v/all/p/first%201/c11913/all/d/v5940%201,v5942%201',
         'period': 'quarterly'
     },
     'pnadct_5442': {
         'url': 'https://apisidra.ibge.gov.br/values/t/5442/n1/all/n2/all/v/all/p/first%201/c888/all/d/v5940%201,v5942%201',
         'period': 'quarterly'
     },
     'pnadct_5444': {
         'url': 'https://apisidra.ibge.gov.br/values/t/5444/n1/all/n2/all/v/all/p/first%201/c694/all/d/v5940%201,v5942%201',
         'period': 'quarterly'
     },
     'pnadct_5606': {
         'url': 'https://apisidra.ibge.gov.br/values/t/5606/n1/all/n2/all/v/all/p/first%201/d/v6294%201,v6296%201',
         'period': 'quarterly'
     },
     'pnadct_5917': {
         'url': 'https://apisidra.ibge.gov.br/values/t/5917/n1/all/n2/all/v/all/p/first%201/c2/all/d/v608%201,v6541%201,v6542%201',
         'period': 'quarterly'
     },
     'pnadct_5918': {
         'url': 'https://apisidra.ibge.gov.br/values/t/5918/n1/all/n2/all/v/all/p/first%201/c58/all/d/v608%201,v6541%201,v6542%201',
         'period': 'quarterly'
     },
     'pnadct_5919': {
         'url': 'https://apisidra.ibge.gov.br/values/t/5919/n1/all/n2/all/v/all/p/first%201/c1568/all/d/v608%201,v6541%201,v6542%201',
         'period': 'quarterly'
     },
     'pnadct_5947': {
         'url': 'https://apisidra.ibge.gov.br/values/t/5947/n1/all/n2/all/v/all/p/first%201/c12027/all/d/v4091%201,v4108%201,v4109%201',
         'period': 'quarterly'
     },
     'pnadct_6371': {
         'url': 'https://apisidra.ibge.gov.br/values/t/6371/n1/all/n2/all/v/all/p/first%201/c2/all/d/v8186%201,v8187%201,v8188%201,v8189%201,v8190%201,v8191%201,v8192%201,v8193%201',
         'period': 'quarterly'
     },
     'pnadct_6372': {
         'url': 'https://apisidra.ibge.gov.br/values/t/6372/n1/all/n2/all/v/all/p/first%201/c58/all/d/v8186%201,v8187%201,v8188%201,v8189%201,v8190%201,v8191%201,v8192%201,v8193%201',
         'period': 'quarterly'
     },
     'pnadct_6373': {
         'url': 'https://apisidra.ibge.gov.br/values/t/6373/n1/all/n2/all/v/all/p/first%201/c1568/all/d/v8186%201,v8187%201,v8188%201,v8189%201,v8190%201,v8191%201,v8192%201,v8193%201',
         'period': 'quarterly'
     },
     'pnadct_6374': {
         'url': 'https://apisidra.ibge.gov.br/values/t/6374/n1/all/n2/all/v/all/p/first%201/c2399/all/d/v8186%201,v8187%201,v8188%201,v8189%201',
         'period': 'quarterly'
     },
    
     'pnadct_6382': {
         'url': 'https://apisidra.ibge.gov.br/values/t/6382/n1/all/n2/all/v/all/p/first%201/c11381/all/d/v8333%201,v8334%201,v8335%201',
         'period': 'quarterly'
     },
     'pnadct_6383': {
         'url': 'https://apisidra.ibge.gov.br/values/t/6383/n1/all/n2/all/v/all/p/first%201/c785/all/d/v8337%201,v8338%201,v8339%201',
         'period': 'quarterly'
     },
     'pnadct_6384': {
         'url': 'https://apisidra.ibge.gov.br/values/t/6384/n1/all/n2/all/v/all/p/first%201/c786/all/d/v8341%201,v8342%201,v8343%201',
         'period': 'quarterly'
     },
     'pnadct_6385': {
         'url': 'https://apisidra.ibge.gov.br/values/t/6385/n1/all/n2/all/v/all/p/first%201/c12043/all/d/v4091%201,v4108%201,v4109%201',
         'period': 'quarterly'
     },
     'pnadct_6386': {
         'url': 'https://apisidra.ibge.gov.br/values/t/6386/n1/all/n2/all/v/all/p/first%201/c12031/all/d/v4091%201,v4108%201,v4109%201',
         'period': 'quarterly'
     },
     'pnadct_6396': {
         'url': 'https://apisidra.ibge.gov.br/values/t/6396/n1/all/n2/all/v/all/p/first%201/c2/all/d/v4099%201,v4103%201,v4114%201,v4115%201,v4116%201,v4117%201,v4118%201,v4119%201',
         'period': 'quarterly'
     },
     'pnadct_6397': {
         'url': 'https://apisidra.ibge.gov.br/values/t/6397/n1/all/n2/all/v/all/p/first%201/c58/all/d/v4099%201,v4103%201,v4114%201,v4115%201,v4116%201,v4117%201,v4118%201,v4119%201',
         'period': 'quarterly'
     },
     'pnadct_6398': {
         'url': 'https://apisidra.ibge.gov.br/values/t/6398/n1/all/n2/all/v/all/p/first%201/c2/all/d/v4093%201,v4110%201,v4111%201,v8345%201,v8347%201,v8349%201,v8351%201,v8353%201,v8355%201,v8386%201,v8387%201,v8388%201,v8389%201,v8390%201,v8391%201,v8392%201,v8393%201,v8394%201,v8395%201,v8396%201,v8397%201',
         'period': 'quarterly'
     },
     'pnadct_6399': {
         'url': 'https://apisidra.ibge.gov.br/values/t/6399/n1/all/n2/all/v/all/p/first%201/c58/all/d/v4093%201,v4110%201,v4111%201,v8345%201,v8347%201,v8349%201,v8351%201,v8353%201,v8355%201,v8386%201,v8387%201,v8388%201,v8389%201,v8390%201,v8391%201,v8392%201,v8393%201,v8394%201,v8395%201,v8396%201,v8397%201',
         'period': 'quarterly'
     },
    
    
    
     #PMC
    
     'pmc_8190': {
         'url': 'https://apisidra.ibge.gov.br/values/t/8190/n1/all/n3/all/v/all/p/first%201/c11046/all/d/v7169%205,v11709%201,v11710%201,v11711%201',
         'period': 'monthly'
     },
     'pmc_8757': {
         'url': 'https://apisidra.ibge.gov.br/values/t/8757/n1/all/n3/all/v/all/p/first%201/c11046/all/d/v7169%205,v7170%205,v11708%201,v11709%201,v11710%201,v11711%201',
         'period': 'monthly'
     },
     'pmc_8880': {
         'url': 'https://apisidra.ibge.gov.br/values/t/8880/n1/all/n3/all/v/all/p/first%201/c11046/all/d/v7169%205,v7170%205,v11708%201,v11709%201,v11710%201,v11711%201',
         'period': 'monthly'
     },
     'pmc_8881': {
         'url': 'https://apisidra.ibge.gov.br/values/t/8881/n1/all/n3/all/v/all/p/first%201/c11046/all/d/v7169%205,v7170%205,v11708%201,v11709%201,v11710%201,v11711%201',
         'period': 'monthly'
     },
     'pmc_8882': {
         'url': 'https://apisidra.ibge.gov.br/values/t/8882/n1/all/n3/all/v/all/p/first%201/c11046/all/c85/all/d/v7169%205,v7170%205,v11708%201,v11709%201,v11710%201,v11711%201',
         'period': 'monthly'
     },
     'pmc_8883': {
         'url': 'https://apisidra.ibge.gov.br/values/t/8883/n1/all/n3/all/v/all/p/first%201/c11046/all/c85/all/d/v7169%205,v7170%205,v11708%201,v11709%201,v11710%201,v11711%201',
         'period': 'monthly'
     },
     'pmc_8884': {
         'url': 'https://apisidra.ibge.gov.br/values/t/8884/n1/all/n3/all/v/all/p/first%201/c11046/all/d/v7169%205,v7170%205,v11708%201,v11709%201,v11710%201,v11711%201',
         'period': 'monthly'
     },
    
     #PMS
    
    #   'pms' : {
    #       'url': '',
    #       'period': ''
    #   }
}


