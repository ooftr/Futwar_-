from flet import*
def main(page:Page):
    page.title ="شجرة فتوار"
    page.window.width = 450
    page.window.height =800
    page.window.max_width=max
    page.window.max_height=main
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.scroll = 'auto'
    page.padding=0
    page.scroll = 'auto'
    page.window.resizable=True
    page.window.title_bar_hidden=True
    im=Column(expand=True,wrap=True,scroll='auto' )
    for i in range(0,10):
        im.controls.append(
            Image(
                src=f"Pcs/{i}.JPG",
                width=page.window.width,
                height=600,
                fit=ImageFit.FILL,
                repeat=ImageRepeat.NO_REPEAT,
                border_radius=border_radius.all(10)
            )
        )   
 
    def close(cls):
        page.window.close()
        return                                  
    page.update()
    def Mypages(vws):
        page.views.clear()              
        page.views.append(
            View(            
                "/",
            [
                Container(
                    Stack([
                        Image(src='Pcs/011.jpg',height=page.window.height,width=page.window.width,fit=ImageFit.FILL,opacity=1),       
                        Container(
                            Column([
                                Column(
                                    spacing=10,
                                    height=page.window.height,
                                    width=page.window.width,
                                    expand=True,
                                    scroll=ScrollMode.HIDDEN,
                                    controls=[
                                    Container(
                                        Row(
                                            alignment=MainAxisAlignment.SPACE_BETWEEN,
                                            controls=[
                                                IconButton(icon=icons.CLOSE,on_click=close,tooltip='إغلاق',icon_color='red',icon_size=20), 
                                                IconButton(icon=icons.SEARCH,tooltip='بحث',icon_color='white',icon_size=20),
                                            ]
                                        ),
                                        padding=padding.only(top=15,left=10,right=10)
                                    ),  
                                    Column([
                                        Row(
                                            alignment = MainAxisAlignment.CENTER,
                                            controls=[  
                                            Text('بسم الله الرحمن الرحيم ',weight='bold',font_family ='Arabic Typesetting',color= colors.WHITE, size=  0.055*page.window.width),
                                            ]
                                        ),
                                        Container(height=0.08*page.window.height),
                                        Row(
                                            alignment = MainAxisAlignment.CENTER,
                                            controls=[    
                                                Text('مرحبا بكم في برنامجنا التعريفي بفتوار ',weight='bold',font_family ='Arabic Typesetting',color= colors.WHITE, size= 0.085*page.window.width),
                                                ]
                                            )
                                    ]),
                                    Container(height=0.045*page.window.height),                               
                                    Row([
                                        ElevatedButton('تعريف عام',width= 0.35*page.window.width,height=0.05*page.window.height,style=ButtonStyle(bgcolor = colors.TEAL_700,color = colors.WHITE),
                                            on_click = lambda _:page.go("/defi")),
                                        ElevatedButton("المعالم والأحياء",width= 0.35*page.window.width,height=0.05*page.window.height,style=ButtonStyle(bgcolor = colors.TEAL_700,color = colors.WHITE),
                                            on_click = lambda _:page.go("/places")),
                                        ],alignment = MainAxisAlignment.CENTER,rtl=True
                                    ),
                                    Row([
                                        ElevatedButton("التعليم والصحة",width= 0.35*page.window.width,height=0.05*page.window.height,style=ButtonStyle(bgcolor = colors.TEAL_700,color = colors.WHITE),
                                            on_click = lambda _:page.go("/ediu")),
                                        ElevatedButton("الأندية والرياضة",width= 0.35*page.window.width,height=0.05*page.window.height,style=ButtonStyle(bgcolor = colors.TEAL_700,color = colors.WHITE),
                                            on_click = lambda _:page.go("/spo")),
                                        ],alignment = MainAxisAlignment.CENTER,rtl=True
                                    ),
                                    Row([
                                        ElevatedButton("أعلام ورموز ",width= 0.35*page.window.width,height=0.05*page.window.height,style=ButtonStyle(bgcolor = colors.TEAL_700,color = colors.WHITE),
                                            on_click = lambda _:page.go("/stars")),
                                        ElevatedButton(" صور مختارة",width= 0.35*page.window.width,height=0.05*page.window.height,style=ButtonStyle(bgcolor = colors.TEAL_700,color = colors.WHITE),
                                            on_click = lambda _:page.go("/img")),
                                        ],alignment = MainAxisAlignment.CENTER,rtl=True
                                    ),
                                            
                                    Container(height=0.035*page.window.height),
                                    Row(
                                        [
                                            Container(
                                                height=0.08*page.window.height,
                                                width=0.7*page.window.width,
                                                border_radius=5,
                                                bgcolor=colors.BLUE_100,
                                                padding=padding.only(top=0,left=15,right=15,bottom=0),
                                                content=Row(
                                                            [
                                                            Text('    '+'الأنساب والمعارف  ',color= colors.BLACK87, size= 25,weight='bold',font_family ='Arabic Typesetting',rtl=True),
                                                            OutlinedButton("دخول",width= 0.17*page.window.width,height=0.05*page.window.height,style=ButtonStyle(color='black',bgcolor = colors.RED_100,shape=RoundedRectangleBorder(radius=3)),
                                                            on_click = lambda _:page.go("/rel")),
                                                            ],alignment=MainAxisAlignment.SPACE_BETWEEN,rtl=True
                                                        )
                                            )
                                        ],alignment = MainAxisAlignment.CENTER
                                    ),
                                    Row(
                                        controls=[
                                            OutlinedButton(" قال صل الله عليه وسلم: { تعلموا من أنسابكم ماتصلون به أرحامكم فإن صلة الرحم محبة في الأهل مثراة في المال منسأة في الأثر } رواه الترمزي وصححه الألباني",width= 0.7*page.window.width,height= 0.12*page.window.height,style=ButtonStyle(padding=10,bgcolor=Colors.BLUE_100,color = colors.BLACK87,shape=RoundedRectangleBorder(radius=10)),disabled=True,
                                                )
                                            ],alignment = MainAxisAlignment.CENTER,rtl=True
                                    ),
                                    Container(height=0.06*page.window.height),
                                    Container(
                                        Row(
                                            controls=[
                                                OutlinedButton("حول البرنامج ",width= 0.3*page.window.width,height= 0.05*page.window.height,style=ButtonStyle(color = colors.WHITE,shape=RoundedRectangleBorder(radius=10)),
                                                on_click = lambda _:page.go("/ediu")),
                                                OutlinedButton("تحديث البرنامج",width= 0.3*page.window.width,height= 0.05*page.window.height,style=ButtonStyle(color = colors.WHITE,shape=RoundedRectangleBorder(radius=10)),
                                                on_click = lambda _:page.go("/ediu")),
                                            ],alignment =MainAxisAlignment.SPACE_BETWEEN,rtl=True
                                        ),
                                        padding=10
                                    )             
                                ])
                            ]),
                        expand=True,
                        )
                    ]),
                expand=True
                )    
           ],padding=0)    
        )#appended_end       
######################################################
######################################################
        if page.route == "/defi":
            page.views.append(
            View(
                "/defi",
                    [  
                        AppBar(title=Text(" معلومات عامة متفرقة",color='black',size=28,weight='bold',font_family='Arabic Typesetting'),center_title=True,
                           bgcolor=colors.RED_300,toolbar_height=50,rtl=True),
                        Container(
                            Column(
                                controls=[
                                Text('  تعتبر قرية فتوار من القرى التي تقع في الاتجاه الغربي لنهر النيل وتوجد في منطقة الباوقة شمال بربر تعتبر قرية فتوار من القرى التي تقع في الاتجاه الغربي لنهر النيل وتوجد في منطقة الباوقة شمال بربر تعتبر قرية فتوار من القرى التي تقع في الاتجاه الغربي لنهر النيل وتوجد في منطقة الباوقة شمال بربر تعتبر قرية فتوار من القرى التي تقع في الاتجاه الغربي لنهر النيل وتوجد في منطقة الباوقة شمال بربر تعتبر قرية فتوار من القرى التي تقع في الاتجاه الغربي لنهر النيل وتوجد في منطقة الباوقة شمال بربر تعتبر قرية فتوار من القرى التي تقع في الاتجاه الغربي لنهر النيل وتوجد في منطقة الباوقة شمال بربر تعتبر قرية فتوار من القرى التي تقع في الاتجاه الغربي لنهر النيل وتوجد في منطقة الباوقة شمال بربر تعتبر قرية فتوار من القرى التي تقع في الاتجاه الغربي لنهر النيل وتوجد في منطقة الباوقة شمال بربر تعتبر قرية فتوار من القرى التي تقع في الاتجاه الغربي لنهر النيل وتوجد في منطقة الباوقة شمال بربر تعتبر قرية فتوار من القرى التي تقع في الاتجاه الغربي لنهر النيل وتوجد في منطقة الباوقة شمال بربر تعتبر قرية فتوار من القرى التي تقع في الاتجاه الغربي لنهر النيل وتوجد في منطقة الباوقة شمال بربر تعتبر قرية فتوار من القرى التي تقع في الاتجاه الغربي لنهر النيل وتوجد في منطقة الباوقة شمال بربر تعتبر قرية فتوار من القرى التي تقع في الاتجاه الغربي لنهر النيل وتوجد في منطقة الباوقة شمال بربر تعتبر قرية فتوار من القرى التي تقع في الاتجاه الغربي لنهر النيل وتوجد في منطقة الباوقة شمال بربر تعتبر قرية فتوار من القرى التي تقع في الاتجاه الغربي لنهر النيل وتوجد في منطقة الباوقة شمال بربر تعتبر قرية فتوار من القرى التي تقع في الاتجاه الغربي لنهر النيل وتوجد في منطقة الباوقة شمال بربر تعتبر قرية فتوار من القرى التي تقع في الاتجاه الغربي لنهر النيل وتوجد في منطقة الباوقة شمال بربر تعتبر قرية فتوار من القرى التي تقع في الاتجاه الغربي لنهر النيل وتوجد في منطقة الباوقة شمال بربر تعتبر قرية فتوار من القرى التي تقع في الاتجاه الغربي لنهر النيل وتوجد في منطقة الباوقة شمال بربر والسلام عليكم ',font_family='adwa-assalaf',size=20,weight='bold',color='black')     
                            ],alignment=MainAxisAlignment.CENTER,scroll='auto',rtl=True),
                            
                            width = page.window.width,
                            height = page.window.height,
                            bgcolor = colors.YELLOW_100, 
                            padding=10
                        )  
                    ],
                scroll = 'auto',
                padding=0
                )
            )#appended_end
        ##########################################################              
        if page.route == "/places":
            page.views.append(
             View(
                "/places",
                    [  
                        AppBar(title=Text("أهم الأماكن والأحياء",color='black',size=28,weight='bold',font_family='Arabic Typesetting'),center_title=True,
                           bgcolor=colors.RED_300,toolbar_height=50,rtl=True),
                        Container(
                            Column([
                                Container(
                                    Text(' قال صل الله عليه وسلم: { تعلموا من أنسابكم ماتصلون به أرحامكم فإن صلة الرحم محبة في الأهل مثراة في المال منسأة في الأثر } رواه الترمزي وصححه الألباني',weight='bold',font_family ='Arabic Typesetting',color= colors.GREEN_900, size= 30,rtl=True)
                                    ,padding=15),
                                Container(height=40),   
                                Row([
                                    OutlinedButton("المشرع الأبيض ",width= 110,height= 35,style=ButtonStyle(bgcolor=colors.RED_200,color = colors.BLACK87,shape=RoundedRectangleBorder(radius=10)),
                                        on_click = lambda _:page.go("/mush")),
                                    OutlinedButton("حلة أبشر ",width=90,height=35,style=ButtonStyle(bgcolor=colors.RED_200,color = colors.BLACK87,shape=RoundedRectangleBorder(radius=10)),
                                        on_click = lambda _:page.go("/absh")),
                                    OutlinedButton("ود إمام ",width= 90,height= 35,style=ButtonStyle(bgcolor=colors.RED_200,color = colors.BLACK87,shape=RoundedRectangleBorder(radius=10)),
                                        on_click = lambda _:page.go("/wde")),
                                    ],alignment =MainAxisAlignment.CENTER,rtl=True),
                                Row([    
                                    OutlinedButton("التضامن ",width=90,height= 35,style=ButtonStyle(bgcolor=colors.RED_200,color = colors.BLACK87,shape=RoundedRectangleBorder(radius=10)),
                                        on_click = lambda _:page.go("/tda")),
                                    OutlinedButton("أبوقرون ",width= 90,height= 39,style=ButtonStyle(bgcolor=colors.RED_200,color = colors.BLACK87,shape=RoundedRectangleBorder(radius=10)),
                                        on_click = lambda _:page.go("/abg")),
                                    ],alignment =MainAxisAlignment.CENTER,rtl=True),    
                            ]),
                            width = page.window.width,
                            height = page.window.height,
                            bgcolor = colors.YELLOW_100, 
                            padding=10
                        )  
                    ],
                scroll = 'auto',
                padding=0
                )
            )#appended_end
        ##########################################################          
        if page.route == "/rel":
            page.views.append(
             View(
                "rel",
                    [  
                        AppBar(title=Text("  الأنساب والأرحام والمعارف",color='black',size=25,weight='bold',font_family='Arabic Typesetting'),center_title=True,
                           bgcolor=colors.RED_300,toolbar_height=50,rtl=True),
                        Container(
                            Column([
                                Container(height=300),   
                                
                            ]),
                            width = page.window.width,
                            height = page.window.height,
                            bgcolor = colors.YELLOW_100, 
                            padding=10
                        )  
                    ],
                scroll = 'auto',
                padding=0
                )
            )#appended_end
        ##########################################################
        if page.route == "/ediu":
            page.views.append(
            View(
                "/defi",
                    [  
                        AppBar(title=Text("التعليم والصحة في فتوار ",color='black',size=25,weight='bold',font_family='Arabic Typesetting'),center_title=True,
                           bgcolor=colors.RED_300,toolbar_height=50,rtl=True),
                        Container(
                            Column([
                            Container(height=300),   
                               
                            ]),
                        width = page.window.width,
                        height = page.window.height,
                        bgcolor = colors.YELLOW_100, 
                        padding=10
                        )  
                    ],
                scroll = 'auto',
                padding=0
                )
            )#appended_end
        ##########################################################
        if page.route == "/spo":
            page.views.append(
            View(
                "/spo",
                    [  
                        AppBar(title=Text("الأندية والمناشط الرياضية ",color='black',size=25,weight='bold',font_family='Arabic Typesetting'),center_title=True,
                           bgcolor=colors.RED_300,toolbar_height=50,rtl=True),
                        Container(
                            Column([
                                Container(height=300),   
                                
                            ]),
                            width = page.window.width,
                            height = page.window.height,
                            bgcolor = colors.YELLOW_100, 
                            padding=10
                        )  
                    ],
                scroll = 'auto',
                padding=0
                )
            )#appended_end
        ##########################################################
        if page.route == "/stars":
            page.views.append(
            View(
                "/stars",
                    [  
                        AppBar(title=Text(" شخصيات وأعلام من فتوار  ",color='black',size=25,weight='bold',font_family='Arabic Typesetting'),center_title=True,
                           bgcolor=colors.RED_300,toolbar_height=50,rtl=True),
                        Container(
                            Column([
                                Container(height=300),   
                                
                            ]),
                            width = page.window.width,
                            height = page.window.height,
                            bgcolor = colors.YELLOW_100, 
                            padding=10
                        )  
                    ],
                scroll = 'auto',
                padding=0
                )
            )#appended_end
        ##########################################################
        if page.route == "/img":
            page.views.append(
            View(
                "/img",
                    [  
                        AppBar(title=Text(" صور منوعة من فتوار",color='black',size=28,weight='bold',font_family='Arabic Typesetting'),center_title=True,
                           bgcolor=colors.RED_300,toolbar_height=50,rtl=True),
                        Container(
                            Stack(
                                controls=[
                                    im,
                                ]
                            )       
                        )  
                    ],
                scroll = 'auto',
                padding=0
                )
            )#appended_end
        ##########################################################
        if page.route == "/mush":
            page.views.append(
            View(
                "/mush",
                    [  
                        Container(       
                            Column([
                                Row([   
                                    IconButton(icon=icons.ARROW_BACK,tooltip='رجوع للخلف',icon_color=colors.BLACK87,icon_size=20,on_click=lambda _:page.go("/places") ),
                                    OutlinedButton(" معلومات مختصرة عن حلة المشرع",width= 220,height= 35,style=ButtonStyle(padding=8,bgcolor=Colors.BROWN_100,color = colors.BLACK87,shape=RoundedRectangleBorder(radius=10)),disabled=True,),             
                                    IconButton(icon=icons.HOME,tooltip='الرئيسية',icon_color=colors.BLACK87,icon_size=20,on_click=lambda _:page.go("/") ),                            
                                ],alignment =MainAxisAlignment.SPACE_BETWEEN,rtl=True),
                                

                            ]),
                        width = page.window.width,
                        height = page.window.height,
                        bgcolor = colors.YELLOW_100, 
                        padding=padding.only(top=18,left=10,right=10,bottom=10)
                        )  
                    ],
                scroll = 'auto',
                padding=0
                )
            )#appended_end
        ##########################################################
        if page.route == "/absh":
            page.views.append(
            View(
                "/absh",
                    [  
                        Container(       
                            Column([
                                Row([   
                                    IconButton(icon=icons.ARROW_BACK,tooltip='رجوع للخلف',icon_color=colors.BLACK87,icon_size=20,on_click=lambda _:page.go("/places") ),
                                    OutlinedButton(" معلومات مختصرة عن حلة أبشر",width= 220,height= 35,style=ButtonStyle(padding=8,bgcolor=Colors.BROWN_100,color = colors.BLACK87,shape=RoundedRectangleBorder(radius=10)),disabled=True,),             
                                    IconButton(icon=icons.HOME,tooltip='الرئيسية',icon_color=colors.BLACK87,icon_size=20,on_click=lambda _:page.go("/") ),                            
                                ],alignment =MainAxisAlignment.SPACE_BETWEEN,rtl=True),
                                

                            ]),
                        width = page.window.width,
                        height = page.window.height,
                        bgcolor = colors.YELLOW_100, 
                        padding=padding.only(top=18,left=10,right=10,bottom=10)
                        )  
                    ],
                scroll = 'auto',
                padding=0
                )
            )#appended_end
        ##########################################################
        if page.route == "/wde":
            page.views.append(
            View(
                "/wde",
                    [  
                        Container(       
                            Column([
                                Row([   
                                    IconButton(icon=icons.ARROW_BACK,tooltip='رجوع للخلف',icon_color=colors.BLACK87,icon_size=20,on_click=lambda _:page.go("/places") ),
                                    OutlinedButton(" معلومات مختصرة عن حلة ودإمام",width= 220,height= 35,style=ButtonStyle(padding=8,bgcolor=Colors.BROWN_100,color = colors.BLACK87,shape=RoundedRectangleBorder(radius=10)),disabled=True,),             
                                    IconButton(icon=icons.HOME,tooltip='الرئيسية',icon_color=colors.BLACK87,icon_size=20,on_click=lambda _:page.go("/") ),                            
                                ],alignment =MainAxisAlignment.SPACE_BETWEEN,rtl=True),
                                

                            ]),
                        width = page.window.width,
                        height = page.window.height,
                        bgcolor = colors.YELLOW_100, 
                        padding=padding.only(top=18,left=10,right=10,bottom=10)
                        )  
                    ],
                scroll = 'auto',
                padding=0
                )
            )#appended_end
        ##########################################################
        if page.route == "/tda":
            page.views.append(
            View(
                "/tda",
                    [     
                        Container(       
                            Column([
                                Row([   
                                    IconButton(icon=icons.ARROW_BACK,tooltip='رجوع للخلف',icon_color=colors.BLACK87,icon_size=20,on_click=lambda _:page.go("/places") ),
                                    OutlinedButton(" معلومات مختصرة عن حلة التضامن",width= 220,height= 35,style=ButtonStyle(padding=8,bgcolor=Colors.BROWN_100,color = colors.BLACK87,shape=RoundedRectangleBorder(radius=10)),disabled=True,),             
                                    IconButton(icon=icons.HOME,tooltip='الرئيسية',icon_color=colors.BLACK87,icon_size=20,on_click=lambda _:page.go("/") ),                            
                                ],alignment =MainAxisAlignment.SPACE_BETWEEN,rtl=True),
                                

                            ]),
                        width = page.window.width,
                        height = page.window.height,
                        bgcolor = colors.YELLOW_100, 
                        padding=padding.only(top=18,left=10,right=10,bottom=10)
                        )  
                    ],
                scroll = 'auto',
                padding=0
                )
            )#appended_end
        ##########################################################
        if page.route == "/abg":
            page.views.append(
            View(
                "/abg",
                    [   
                        Container(       
                            Column([
                                Row([   
                                    IconButton(icon=icons.ARROW_BACK,tooltip='رجوع للخلف',icon_color=colors.BLACK87,icon_size=20,on_click=lambda _:page.go("/places") ),
                                    OutlinedButton(" معلومات مختصرة عن حلة أبوقرون",width= 220,height= 35,style=ButtonStyle(padding=8,bgcolor=Colors.BROWN_100,color = colors.BLACK87,shape=RoundedRectangleBorder(radius=10)),disabled=True,),             
                                    IconButton(icon=icons.HOME,tooltip='الرئيسية',icon_color=colors.BLACK87,icon_size=20,on_click=lambda _:page.go("/") ),                            
                                ],alignment =MainAxisAlignment.SPACE_BETWEEN,rtl=True),
                                

                            ]),
                        width = page.window.width,
                        height = page.window.height,
                        bgcolor = colors.YELLOW_100, 
                        padding=padding.only(top=18,left=10,right=10,bottom=10)
                        )  
                    ],
                scroll = 'auto',
                padding=0
                ), 
        
            )#appended_end
        ##########################################################
       
        page.update()
    def back(bck): 
        page.views.pop()
        bc=page.views[-1]
        page.go(bc.route)
    page.on_route_change = Mypages
    page.on_view_pop = back
    page.go(page.route)
app(main)
