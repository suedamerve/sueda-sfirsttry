word_list ={
        "abandon": ["terk etmek", "bırakmak", "vazgeçmek"],
        "fraud": ["sahtekarlık","dolandırıcılık","aldatma"],
        "absorb": ["almak","kavramak","anlamak","emmek"],
       "alongside": ["yanına,yanı sıra,yan yana"],
       "associate": ["ilişkilendirmek","birleştirmek","iş arkadaşı"],
       "framework": ["kadro","karkas","çerçeve"],
       "assumption": ["sanı","farzetme","varsayım"],
       "mass": ["yığmak","kümelemek","kitle"],
        "chase": ["peşinde olmak","kovalamak","takip etmek"],
        "bond": ["tutturmak","birleştirmek","bağ"],
        "enquiry": ["sorgu","soru","soruşturma"],
        "hollow": ["oyuk","çukur","içi boş"],
        "fundamental": ["esas","asli","esas"],
        "demand": ["talep etmek","talepte bulunmak","talep"],
        "derive": ["türemek","-den elde etmek","yola çıkmak]"],
        "crop": ["mahsul","ekin","kesmek"],
        "imply": ["ima etmek","kastetmek","göstermek"],
        "decent": ["edepli","iyi","düzgün"],
        "excessive": ["haddinden fazla","aşırı","aşkın"],
        "genuinely": ["gerçekten","gerçek olarak","canıgönülden"],
        "implement": ["yerine getirmek","uygulamak","alet-edevat"],
        "fellow": ["herif","hemcins","bir bilim kurumunun üyesi"],
        "broadly": ["açık olarak","belli","geniş"],
        "justify": ["savunmak","suçsuzluğunu kanıtlamak","hak vermek"],
        "accurately": ["kesin olarak","tam olarak","doğru olarak"],
        "accomplish": ["başarıyla tamamlamak","sonuçlandırmak","sonunu getirmek"],
        "bias": ["önyargı","aklını çelmek","bir tarafa etki etmek"],
        "incident": ["hadise","olay","yük"],
        "briefly": ["kısaca","kısaca","muhtasar biçimde"],
        "conspiracy": ["komplo","gizli anlaşma","suikast"],
        "devote": ["adamak","vakfetmek","adamak"],
        "exclude": ["dışlamak","hariç tutmak","dahil etmemek"]}
        
wrong_answers = {}

for word in word_list:
    answer = input("\nWrite Turkish meaning of " + word + ": ") 
    
    if answer in word_list[word]:
        print("True")
    else:
        print("False") 
        wrong_answers[word] = word_list[word]

print("*********** \nThese are your wrong_answers : \n", wrong_answers, "\n*************")

choosing = input("Do you want to back your wrong answer Y/N: ")
if choosing == "Y" or choosing == "y":
    for wrong_answer in wrong_answers:
        new_answer = input("\nWrite again Turkish meaning of " + wrong_answer + ": ")
        
        if new_answer in wrong_answers[wrong_answer]:
            print("True")
        else:
            print("False")   
else:
    quit()




    

