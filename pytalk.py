from discord import Webhook, RequestsWebhookAdapter

print("""
           .,                    ,-·-.          ,'´¨;             ,  . .,  °                    ,.,   '               ,.  '                            _  °  
   ,·´    '` ·.'              ';   ';\      ,'´  ,':\'     ;'´    ,   ., _';\'                ;´   '· .,            /   ';\             ,.·,       :´¨   ;\   
    \`; `·;·.   `·,           ;   ';:\   .'   ,'´::'\'    \:´¨¯:;'   `;::'\:'\             .´  .-,    ';\        ,'   ,'::'\          ,'   ,'\     .'´ ,·´::'\  
     ;   ,'\::`·,   \'         '\   ';::;'´  ,'´::::;'       \::::;   ,'::_'\;'            /   /:\:';   ;:'\'     ,'    ;:::';'         ;'  ,'::\ .·' .·´::::::;' 
    ;   ,'::'\:::';   ';          \  '·:'  ,'´:::::;' '           ,'  ,'::;'  ‘            ,'  ,'::::'\';  ;::';     ';   ,':::;'          ;  ;::·´ .·´:::::::;·´  
    ;   ;:::;'·:.'  ,·'\'          '·,   ,'::::::;'´             ;  ;:::;  °        ,.-·'  '·~^*'´¨,  ';::;     ;  ,':::;' '         ';  '´   ;´::::::;·´      
   ';  ';: -· '´. ·'´:::'\'          ,'  /::::::;'  '             ;  ;::;'  ‘         ':,  ,·:²*´¨¯'`;  ;::';    ,'  ,'::;'            ;  ;'\   '\::;·´          
   ;  ,-·:'´:\:::::::;·'         ,´  ';\::::;'  '               ;  ;::;'‚           ,'  / \::::::::';  ;::';    ;  ';_:,.-·´';\‘    ;  ;:\:'·.  '·., ,.·';'     
  ,'  ';::::::'\;:·'´             \`*ª'´\\::/‘                  ',.'\::;'‚          ,' ,'::::\·²*'´¨¯':,'\:;     ',   _,.-·'´:\:\‘   ;_;::'\::`·._,.·'´:\'     
  \·.,·\;-· '´  '                 '\:::::\';  '                  \::\:;'‚          \`¨\:::/          \::\'      \¨:::::::::::\';   \::'\:;' '·::\::\:::::'\    
   \::\:\                          `*ª'´‘                       \;:'      ‘       '\::\;'            '\;'  '     '\;::_;:-·'´‘      '\::\     `·'\::\;:·'´'    
    `'·;·'                            '                            °                `¨'                          '¨                 ¯          ¯'         
     """)
actWeb = input("Webhook : ")
webhook = Webhook.from_url(actWeb, adapter=RequestsWebhookAdapter())
talk = input("Say : ")
webhook.send(talk)