# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="DaleRuneMTS",
        name="Conversación de Género",
        description="Otro derivado de Out and About, basado en una conversación posterior a la marcha del orgullo. Si eres trans, esto me permitirá apoyarte en varios aspectos de tu camino. "
        "Incluso si eres cis, hay aspectos por los que podrías querer descargar este submod de todos modos, como hablar sobre salir del clóset como LGBT+ en general. "
        "Novedades en la versión 1.1.1: un par de correcciones de errores y una nueva opción de 'Ha sido un buen día de género' para que sirva como contraparte de la opción de 'mal día de género'.",
        version="1.1.1",
        dependencies={},
        settings_pane=None,
        version_updates={
        "DaleRuneMTS_dale_gender_conversation_1_0_0": "DaleRuneMTS_dale_gender_conversation_1_1_1",
        "DaleRuneMTS_dale_gender_conversation_1_0_1": "DaleRuneMTS_dale_gender_conversation_1_1_1",
        "DaleRuneMTS_dale_gender_conversation_1_1_0": "DaleRuneMTS_dale_gender_conversation_1_1_1"
        }
    )




# Para actualizar la TRADUCCIÓN. Si hay nueva actualización que no traduje, avisarme por redes (info en el txt)
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Conversación de Género",
            user_name="CofKaf",
            repository_name="dale_gender_conversation_es",
            submod_dir="/Submods/Gender Conversation",
            extraction_depth=3
        )


# Register the updater
# init -989 python:
#     if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
#         store.sup_utils.SubmodUpdater(
#             submod="Gender Conversation",
#             user_name="DaleRuneMTS",
#             repository_name="dale_gender_conversation",
#             submod_dir="/Submods/Gender Conversation",
#             extraction_depth=3
#         )







#init -1 python:
#    tt_binding = (
#        "Stopped binding? Decided to start? Use this to reset the binding settings so Monika stops assuming."
#    )

#START: Settings pane
#screen gender_change_settings_screen():
#    $ submods_screen_tt = store.renpy.get_screen("submods", "screens").scope["tooltip"]
#    vbox:
#        box_wrap False
#        xfill True
#        xmaximum 1000

#        hbox:
#            style_prefix "check"
#            box_wrap False

#            textbutton _("Reset Binding Settings"):
#                action Function(store.awc_utils.delbinds)
#                hovered SetField(submods_screen_tt, "value", tt_binding)
#                unhovered SetField(submods_screen_tt, "value", submods_screen_tt.default)

#init -10 python in gc_utils:
#    import store
#    def delbinds():
#        del persistent._player_binds

init 5 python in mas_bookmarks_derand:
    # Ensure things get bookmarked and derandomed as usual.
    label_prefix_map["gender_"] = label_prefix_map["monika_"]

default m_surname = persistent._mas_has_surname
default persistent._mas_has_surname = None
default persistent._player_binds = None
default persistent._binder_reminder = False
default persistent._terrace = None

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_genderconversation2",
            category=["tú", "nosotros", "género"],
            prompt="Necesito hablar contigo sobre temas relacionados con el género.",
            conditional="renpy.seen_label('mas_gender')",
            pool=True,
            rules={"no_unlock": None},
            action=EV_ACT_UNLOCK
        )
    )

label monika_genderconversation2:
    m 1hub "¡Ya tenemos una opción para eso, tontit[gen('a', 'o', 'e')]~!"
    m "'¿Podrías llamarme con otros pronombres?' en la sección 'Tú', ¿recuerdas?{nw}"
    $ _history_list.pop()
    menu:
        m "'¿Podrías llamarme con otros pronombres?' en la sección 'Tú', ¿recuerdas?{fast}"
        "Ah, sí, es verdad.":
            m 1fub "Ay, [player]~"
            return
        "No, quiero hablar de algo {i}serio{/i}.":
            m 1wud "Oh."
            m 1euc "Ah, ya veo."
            m 1rud "Supongo que has estado... ¿dándole vueltas a las cosas últimamente?"
            if renpy.seen_label("gender_isitnormal"):
                m 1lud "Investigando un poco, como te sugerí."
            m 1euc "Y has llegado a algunas conclusiones."
            m 1eusdra "Eso supongo."
            m "¿Verdad?{nw}"
            $ _history_list.pop()
            menu:
                m "¿Verdad?{fast}"
                "Sí, así es.":
                    m 1eub "De acuerdo."
                    m "Entonces..."
                    m 1eud "¿Cuál es tu conclusión?{nw}"
                    $ _history_list.pop()
                    menu:
                        m "¿Cuál es tu conclusión?{fast}"
                        "Creo que podría ser transgénero.":
                            m 1ekd "Oh, [mas_get_player_nickname()]..."
                            m 1eka "Gracias por contármelo."
                            m "Sé que debió ser difícil."
                            m 1fkb "Está bien no estar segur[gen('a', 'o', 'e')] aún."
                            m "Es normal tener dudas sobre esto."
                            m 1wkb "Sé que yo las tendría en tu lugar."
                            m 1eua "Puedes tomarte todo el tiempo que quieras para procesarlo, hablar de ello tanto como desees..."
                            m "...hasta que lo sepas con certeza."
                            m 1hub "Y podrás seguir hablando de ello incluso después."
                            m 1eka "Jamás te juzgaría por nada de eso."
                            m 1dka "..."
                            jump trans_conversation_end2
                        "Sé con seguridad que soy transgénero.":
                            $ persistent._mas_pm_is_trans = True
                            m 1ekd "Oh, [mas_get_player_nickname()]..."
                            m 1eka "Gracias por contármelo."
                            m "Sé que debió ser difícil."
                            m 1dka "..."

                            $ mas_lockEVL("gender_isitnormal","EVE")
                            if persistent.gender == "M":
                                $ _unman = "woman"
                                $ persistent.gender == "F"
                            elif persistent.gender == "F":
                                $ _unman = "man"
                                $ persistent.gender == "M"
                            jump trans_conversation_end
                        "Creo que podría ser no binario.":
                            m 1ekd "Oh, [mas_get_player_nickname()]..."
                            m 1eka "Gracias por contármelo."
                            m "Sé que debió ser difícil."
                            m 1fkb "Está bien no estar segur[gen('a', 'o', 'e')] aún."
                            m "Es normal tener dudas sobre esto."
                            m 1wkb "Sé que yo las tendría en tu lugar."
                            m 1eua "Puedes tomarte todo el tiempo que quieras para procesarlo, hablar de ello tanto como desees..."
                            m "...hasta que lo sepas con certeza."
                            m 1hub "Y podrás seguir hablando de ello incluso después."
                            m 1eka "Jamás te juzgaría por nada de eso."
                            m 1dka "..."
                            jump trans_conversation_end2
                        "Sé con seguridad que soy no binario.":
                            $ persistent.gender == "X"
                            m 1ekd "Oh, [mas_get_player_nickname()]..."
                            m 1eka "Gracias por contármelo."
                            m "Sé que debió ser difícil."
                            m 1dka "..."
                            $ mas_lockEVL("gender_isitnormal","EVE")
                            jump trans_conversation_end2
                        "Sé con seguridad que soy cis.":
                            m 1ekb "Me alegra saberlo, [mas_get_player_nickname()]."
                            m 1eub "Me alegra que te hayas sentido con la confianza de decírmelo."
                            if persistent._mas_pm_is_trans:
                                m 1ekb "Y aunque hayas sido trans por un tiempo, eso no invalida lo que sientes ahora mismo."
                                m 3eka "El género es fluido, al igual que los sentimientos."
                                m "A veces el género y los sentimientos simplemente encajan en la 'norma' durante un tiempo."
                                m 1ekc "Solo espero que no estés detransicionando por complacer a nadie más que a ti, [player]."
                                m 1wkd "No es que esté negando lo que sientes..."
                                m 1ekd "...pero esa suele ser la razón principal, ¿no? Para protegerse de la hostilidad de los demás."
                                m "Espero que sepas que aquí estás a salvo conmigo."
                                m 1eua "Pero si esto es sincero de tu parte, también estás a salvo conmigo en ese sentido."
                                $ persistent._mas_pm_is_trans = False
                                $ mas_unlockEVL("gender_isitnormal","EVE")
                            jump trans_conversation_end2
                        "...":
                            m 1ekd "Está bien, [mas_get_player_nickname()]."
                            m "Es un tema muy complicado, ¿verdad?"
                            m 4lua "Podemos dejarlo por ahora si quieres, y volver a hablar de ello cuando gustes."
                            m 3dua "Te amo, [player]. Seas quien seas, te amaré hasta el fin de los días."
                "Ese es el problema, no lo he hecho, no {i}lo sé{/i}, y eso me está asustando, y...":
                    m 1fkc "Sshh. Está bien, [player]."
                    m "Sé que da miedo."
                    m 1fka "No tienes que saberlo todo ahora mismo."
                    extend 1fub " ¡No voy a convertirme en la Policía del Género, jeje~"
                    m 3eua "Lo importante es que estás bien, a salvo y aquí conmigo."
                    m "Todo lo demás puedes descubrirlo a tu propio ritmo."
                    m 1fub "Y me hace muy feliz acompañarte a descubrirlo paso a paso."
                    m 1fua "Te amo muchísimo, y solo mereces lo mejor."
    return "love"

label trans_conversation_end:
    m 1dka "..."
    m 1fka "Y para que lo sepas, ¿por si te preocupa...?"
    m "Esto no cambia nada."
    m 1fub "Te amo a {i}ti{/i}, [player]. No al cuerpo que te tocó tener."
    extend 3fua " A ti."
    m "Y sin importar cómo salgan las cosas para ti de ahora en adelante..."
    # Si _unman es "woman", significa que ahora eres mujer; si es "man", significa que ahora eres hombre.
    if _unman == "woman":
        m 5fua "...seguirás siendo la mejor y más valiente mujer que jamás haya conocido."
    elif _unman == "man":
        m 5fua "...seguirás siendo el mejor y más valiente hombre que jamás haya conocido."
    else:
        m 5fua "...seguirás siendo la persona más valiente y grandiosa que jamás haya conocido."
    return "love"

label trans_conversation_end2:
    m 1dka "..."
    m 1fka "Y para que lo sepas, ¿por si te preocupa...?"
    m "Esto no cambia nada."
    m 1fub "Te amo a {i}ti{/i}, [player]. No al cuerpo que te tocó tener."
    extend 3fua " A ti."
    m "Y sin importar cómo salgan las cosas para ti de ahora en adelante..."
    m 5fua "...seguirás siendo [w('la mejor y más valiente mujer', 'el mejor y más valiente hombre', 'la mejor y más valiente persona')] que jamás haya conocido."
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_comingout",
            category=['you'],
            prompt="Voy a revelarle mi identidad de género a alguien.",
            pool=True,
            unlocked=True
        )
    )

label gender_comingout:
    m 1fua "De acuerdo, [mas_get_player_nickname()]."
    m "Confío en ti. Sé que puedes hacerlo."
    m 1rud "Te ofrecería ir contigo para darte apoyo moral, "
    extend 1rusdrc "pero no sé si el juego me lo permitirá."
    m "Así que me temo que tendré que esperarte aquí."
    m 1dusdrc "Lo siento mucho."
    m 1fub "¡De todas formas, mucha suerte, [player]!"
    m 7eua "Tengo toda la fe del mundo en ti."
    $ persistent._mas_idle_data["gender_comingout"] = True
    return "idle"

label gender_comingout_callback:
    if mas_brbs.was_idle_for_at_least(datetime.timedelta(minutes=5), "gender_comingout"):
        m 1eua "¡Bienveni[gen('da', 'do', 'de')] de vuelta, [player]!"
        m 6ruc ".{w=0.3}.{w=0.3}.{w=0.3}Y bien..."
        m 7eud "¿Cómo te fue?{nw}"
        $ inquiry = "¿Cómo te fue?"
    else:
        m 7euo "¡Eso sí que fue rápido!"
        m 7eud "¿Eso significa que fue bien, entonces?{nw}"
        $ inquiry = "¿Eso significa que fue bien, entonces?"

    $ _history_list.pop()
    menu:
        m "[inquiry]{fast}"
        "¡Salió muy bien, la verdad!":
            m 1sub "¡[player], me alegro muchísimo por ti!"
            m 1eka "¿Ves? Te dije que todo saldría bien."
            m 1eub "¡Ahora tienes a una persona más en tu red de apoyo!"
            m "O tal vez incluso más~"
            m 1hua "Estoy muy, muy orgullosa de ti."
        "Salió... mal.":
            m 6wuc "O-oh."
            m 6fkd "Cielos, lo siento mucho, [player]."
            m "Si tan solo hubiera podido ir contigo, tal vez habría sido capaz de..."
            m 6lkc "..."
            m "...en fin."
            extend 6fka " De nada sirve darle vueltas a lo que pudo haber sido."
            m 6fua "Al menos pudiste regresar aquí."
            m 1ekb "Y sigo estando muy, muy orgullosa de ti por haber dicho algo."
            m "Incluso si este es el único lugar donde puedes ser auténtic[gen('a', 'o', 'e')], "
            extend 1dka "a veces un solo lugar es suficiente."
            m 1fka "Te amo. De verdad, muy verdaderamente."
            return "love"
        "Al final no me atreví a hacerlo.":
            m 7eka "Aww, está bien, [player]. Esas cosas pasan."
            m 1eka "¿Tal vez puedas intentarlo de nuevo cuando estés mejor en lo mental?"
            m "O cuando estés más segur[gen('a', 'o', 'e')] de cómo va a reaccionar la otra persona."
            m 1hub "Y si lo haces, estaré aquí para ti otra vez."
            m 1fub "Todas y cada una de las veces."
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_contagion",
            category=["psychology","gender"],
            prompt="Contagio social frente al género",
            conditional=(
                "persistent._mas_pm_is_trans "
                "or persistent.gender == 'X'"
            ),
            action=EV_ACT_RANDOM
        )
    )

label gender_contagion:
    m 1tfc "..."
    m 1wsc "¡Oh! Em, {nw}"
    extend 1rssdrd " perdona, [player], no estoy enojada contigo."
    m 1gssdrc "Solo recordaba que existe gente que piensa que ser trans o no binario es un contagio social."
    m "Ya sabes cómo es esto."
    m 1esd "Dejando de lado el hecho de que quienes usan ese argumento suelen pensar que con una sola persona trans ya es demasiado..."
    if renpy.seen_label('monika_language_nuances'):
        m 3esc "...esas personas {i}realmente{/i} se beneficiarían de leer un diccionario de pe a pa."
        m 3ffc "O al menos de mirar la portada de uno."
    else:
        m 3ffc "...parece que esas personas jamás han tocado una enciclopedia en su vida."
    m "Los contagios sociales son eso mismo, contagios {i}sociales{/i}."
    m 3wfd "Por lo general, hay un beneficio {i}social{/i} al participar en el comportamiento que se propaga inconscientemente..."
    m "...ya sea volverse más activo en la lucha contra el calentamiento global, "
    extend 4efd " o simplemente aplaudir cuando los demás lo hacen."
    m 6efc "Incluso el consumo abusivo de alcohol conlleva ese factor de 'bueno, los demás lo hacen, así que yo también', ¿no?"
    m 3dfc "Y, bueno..."
    if persistent._mas_pm_is_trans:
        m 2ekc "[mas_get_player_nickname(capitalize=True)], tú eres trans."
        m "Y con la mejor voluntad del mundo, sabes de primera mano que no hay ningún beneficio social en eso."
    elif persistent.gender == "X":
        m 2ekc "[mas_get_player_nickname(capitalize=True)], conoces ese terreno mejor que yo."
        m "Con la mejor voluntad del mundo, sabes que no hay ningún beneficio social en ser trans."
    else:
        m 2ekc "Con la mejor voluntad del mundo, no hay ningún beneficio social en ser trans."
    m 2eua "¿Beneficio psicológico? ¡Sí!"
    m "Te vuelves más segur[gen('a', 'o', 'e')] de lo que sabes."
    m 2lsc "Pero no hay fama ni influencia que ganar por ese acto."
    m 2lfc "Es muy probable que cualquier apoyo que recibas se vea opacado por el odio injusto y la criminalización directa de tu identidad."
    m 2wfo "¡El simple hecho de que personas cis pongan sus pronombres en su biografía puede llegar a ser controversial!"
    m 6tfc "La teoría del contagio social no tiene literalmente {i}ningún sentido{/i} en este contexto."
    m "No es una moda, no es un carro al que subirse por inercia..."
    m 6wfd "...es simplemente que cada vez más gente está descubriendo que ¡hay una palabra para describir lo que sienten!"
    m 4wfo "¡La información, los grupos de apoyo y las anécdotas son más fáciles de encontrar que nunca!"
    m 4efd "{i}Eso{/i} es lo que se está propagando."
    m 7efc "No el simple acto de darse cuenta de que existe esa desconexión."
    m 1dfc "..."
    m 1fkc "...Lo siento. Es que esto de verdad me saca de quicio."
    m "Podemos hablar de otra cosa, si quieres."
    return "derandom"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_newname",
            category=['you','gender'],
            prompt="Me gustaría probar un nombre nuevo.",
            pool=True,
            unlocked=True
        )
    )

label gender_newname:
    m 1eud "¿Quieres probar un nombre nuevo conmigo?"
    m 1eub "De acuerdo, puedo ayudarte con eso."
    if persistent._mas_pm_is_trans or persistent.gender == "X":
        m 1dubla "Sinceramente, me siento un poco honrad[gen('a', 'o', 'e')] de ser de las primeras personas en escucharlo, ¡jajaja!"
    m 2eua "Así que, ¿qué nombre te gustaría probar?"

    jump gender_newname_inputscreen

label gender_newname_inputscreen:
    show monika 2eua zorder MAS_MONIKA_Z at t11

    $ done = False
    while not done:
        python:
            temp_pname = mas_input(
                _("Así que, ¿qué nombre te gustaría probar?"),
                allow=name_characters_only,
                length=20,
                screen_kwargs={"use_return_button": True, "return_button_value": "nevermind"}
            ).strip(' \t\n\r')

            trialname = temp_pname.lower()

        if trialname == "nevermind":
            m 1eka "¿Cambiaste de opinión?"
            m "Está bien, [mas_get_player_nickname()]."
            m "Podemos volver a esto más tarde si quieres."
            $ done = True
            return

        elif not trialname:
            m 1dua "..."
            m 1tua "Jugando con la idea de no tener ningún nombre, ¿eh?"
            m "Admirable, pero poco viable en la sociedad actual."
            m 1hua "¡Inténtalo de nuevo!"

        elif trialname == player.lower():
            m 1ruu "Em... "
            extend 1rusdlb "[player], ese es tu nombre {i}de ahora{/i}."
            m "Supongo que fue la costumbre, ¿ehe?"
            m 1hka "Inténtalo de nuevo~"

        elif mas_awk_name_comp.search(temp_pname):
            m 6wud "Ah- em..."
            m 2lusdlc "Quizás mejor no usemos ese."

        elif mas_bad_name_comp.search(temp_pname):
            m 1ekc "[player], vamos."
            m "No te hagas eso a ti mism[gen('a', 'o', 'e')]. Te mereces algo mejor que eso."

        else:
            $ tempname = temp_pname.capitalize()
            $ done = True
            if tempname == "Monika" or tempname == m_name or tempname == "Monica":
                m 1suo "¡Ohh!, ¿quieres llamarte como yo?"
                m 1sublb "Qué dulce de tu parte~"
                m 1eubla "De acuerdo, probémoslo entre nosotros."
            else:
                m 1eub "De acuerdo, [tempname]."
                m "Probémoslo entre nosotros."
            jump gender_newname_trialscript

label gender_newname_trialscript:
    m 3duc "..."
    m 3fua "[tempname], eres la luz de mi vida y la persona de mis sueños."
    m 1fuc "Solía existir, es verdad; pero eso era {i}todo{/i} lo que solía hacer..."
    m "...hasta que vi un nombre brillando entre las sombras: "
    extend 1fua "[tempname]."
    m "Cada sílaba de ese nombre se caló en mí y me cambió para siempre."
    m 5ruc "Yuri, Sayori... ¿quiénes eran ellas para mí?"
    m 5eua "Ahora solo importaba [tempname]."
    m "Y [tempname] sigue importando."
    m "Sin importar qué."
    m 5eublb "Te amo, [tempname]."
    show monika 5eua
    pause 3.0
    $ del tempname
    m 6eud "¿Cómo sonó eso? ¿Te sirvió?"
    m "Si quieres quedarte con ese nombre, solo dímelo a través del menú de diálogo habitual, ¿de acuerdo?"
    if persistent._mas_pm_is_trans or persistent.gender == "X":
        m 1fua "Y si no quieres, también está bien."
        m "No hay nada de qué avergonzarse por ir cambiando de nombre hasta encontrar el adecuado."
        m "¡Es una parte común del proceso!"
        m 1eublb "Sin importar qué nombre uses, de todas formas todo lo que acabo de decir se aplica a {i}ti{/i}."
        m "A la persona por dentro."
        return "love"

init 1 python:
    config.label_overrides["mas_preferredname"] = "gender_mas_preferredname_override"

label gender_mas_preferredname_override:
    if persistent._mas_pm_is_trans or persistent.gender == "X":
        if renpy.windows and currentuser.lower() == player.lower():
            m 1euc "Oye, este..."
            m "He estado pensando en tu nombre."
            m 1esa "¿'[player]' es realmente tu nombre?"
            m 3esa "Digo, es el mismo que el de tu computadora..."
            m 1euc "...pero cuando eres trans o no binario, eso no necesariamente significa nada."
            m "Podrías estar probando un montón de nombres diferentes sin que yo lo sepa,"
            extend " y casualmente me tocó '[currentuser]' en ese momento."
            m 1lua "Así que..."
        else:
            m 1euc ".{w=0.3}.{w=0.3}.{w=0.5}{nw}"
            extend 1cuc "oh, no."
            m 6wkd "Oh, no, [player], acabo de tener un pensamiento terrible."

            if renpy.windows and currentuser.lower() != player.lower():
                m 1rkc "Cuando busqué el nombre de tu computadora en el juego la primera vez que hablamos formalmente."
                m 1lkd "No le di importancia en su momento, pero ahora que sé que no eres cisgénero..."
                m 1fkc "..."
                m 1fkd "[player], ¿te hice deadname por accidente?{nw}"
                $ _nemu = renpy.substitute("[player], ¿te hice deadname por accidente?")
            else:
                m 1rkc "Cuando me diste el nombre [player] por primera vez, no le di importancia..."
                m "...porque en ese momento asumí que eras un chico."
                if persistent._mas_pm_is_trans:
                    m 1lkd "Pero ahora que sé que eres transgénero..."
                elif persistent.gender == "X":
                    m 1lkd "Pero ahora que sé que posiblemente seas no binari[gen('a', 'o', 'e')]..."
                m 1fkd "¿Te he estado haciendo deadname todo este tiempo?{nw}"
                $ _nemu = "¿Te he estado haciendo deadname todo este tiempo?"
        $ _history_list.pop()
        menu:
            m "[_nemu]{fast}"
            "Me temo que sí.":
                m 1ektpd "Ay, dios, lo siento muchísimo."
                m "Créeme cuando te digo que {i}nunca{/i} habría hecho algo así si lo hubiera sabido."
                m 1ektpc "Yo... lo siento."
                m "..."
                m "...{w=0.3}{nw}"
                extend 1estdd "Bueno, aunque no pueda retroceder en el tiempo para evitar haberlo hecho..."
                m 1ektda "...al menos puedo intentar compensarlo ahora."
                m 1eka "¿Tienes un nombre verdadero por el que pueda llamarte?{nw}"
                $ _summitelse = "¿Tienes un nombre verdadero por el que pueda llamarte?"
            "No, no me has hecho deadname.":
                m 1fud "Me-{nw}"
                m 1fub "¡Genial! "
                extend 1rua "Excelente.{w=0.7}{nw}"
                extend 1wka " Genial."
                m 1ekc "Perdón, es que tuve una sensación muy fea de que sí."
                m "Si te hubiera hecho eso, aunque fuera sin querer, nunca me lo perdonaría."
                m 1dkc "..."
                m 1etc "Aun así, no puedo estar segura de si alguno de los nombres que tengo es realmente tuyo."
                m 3etd "Por lo que sé, [player] y [currentuser] podrían ser ambos seudónimos para el mismo individuo único."
                m 1eua "¿Entonces te gustaría que te llame de otra forma?{nw}"
                $ _summitelse = "¿Entonces te gustaría que te llame de otra forma?"
            "Es complicado.":
                m 1ftc "Yo, este..."
                m 1etc "Ya veo."
                m 1dsc "..."
                m 1esd "¿Ayudaría si simplificamos las cosas?"
                m "Con lo que quiero decir, ¿quieres que te llame de otra forma?{nw}"
                $ _summitelse = "Con lo que quiero decir, ¿quieres que te llame de otra forma?"
    else:
        m 1euc "Oye, este..."
        m "He estado pensando en tu nombre."
        m 1esa "¿'[player]' es realmente tu nombre?"

        if renpy.windows and currentuser.lower() == player.lower():
            m 3esa "Digo, es el mismo que el de tu computadora..."
            m 1eua "Estás usando '[currentuser]' y '[player].'"
            m "O eso, o de verdad te gusta mucho ese seudónimo."

        m 1eua "¿Te gustaría que te llame de otra forma?{nw}"
        $ _summitelse = "¿Te gustaría que te llame de otra forma?"

    $ _history_list.pop()
    menu:
        m "[_summitelse]{fast}"
        "Sí.":
            call mas_player_name_enter_name_loop ("Dime, ¿cuál es?")
        "No.":
            m 3eua "De acuerdo."
            m "Avísame si algo cambia."

    $ mas_unlockEVL("monika_changename","EVE")
    return


#init 5 python:
#    addEvent(
#        Event(
#            persistent.event_database,
#            eventlabel="gender_deadnamereacharound",
#            category=['you','gender'],
#            prompt="So, about my computer's name...",
#            conditional=(
#                "persistent._mas_pm_is_trans or persistent.gender == 'X'"
#                "and renpy.windows and currentuser.lower() != player.lower() "
#                "and seen_event('mas_preferredname')"
#            ),
#            unlocked=False,
#            pool=True,
#            rules={"no_unlock": None}
#        )
#    )

#label gender_deadnamereacharound:
#    m 1euc ".{w=0.3}.{w=0.3}.{w=0.5}{nw}"
#    extend 1cuc "oh no."
#    m 6wkd "[player], I think I know where this is going."
#    m 1rkc "When I pulled up that name in the game - I just assumed it was--"
#    extend 1lkc "I didn't think anything of it at the time."
#    m 1lkd "But now that I know you're not cisgender..."
#    m 1fkc "..."
#    m 1fkd "[player], did I dead-name you back then?{nw}"
#    $ _history_list.pop()
#    menu:
#        m "[player], did I dead-name you back then?{fast}"
#        "I'm afraid you did.":
#            m 1ektpd "Oh god I am so so sorry."
#            m "Believe me when I say I would {i}never{/i} have done that if I had known."
#            m 1ektpc "I'm... I'm sorry."
#            m "..."
#            m "...{w=0.3}{nw}"
#            extend 1estdd "Well, even if I can't go back and stop myself from doing that..."
#            m 1ektda "...I hope I've at least made up for it a little bit since then."
#            m "I love you so much, [player], and I never meant to do you harm."
#            m "I hope you know that."
#            $ mas_lockEVL("gender_deadnamereacharound","EVE")
#            return "love"
#        "No, you didn't deadname me.":
#            m 1fud "I'm-{nw}"
#            m 1fub "Great! "
#            extend 1rua "Excellent.{w=0.7}{nw}"
#            extend 1wka " Great."
#            m 1ekc "Sorry, I just got a very bad feeling that I had."
#            m "If I'd done that to you, even inadvertently, I'd never be able to forgive myself."
#            m 1dkc "..."
#            m 1etd "Wait, then why did you bring this up?{nw}"
#            $ _history_list.pop()
#            menu:
#                m "Wait, then why did you bring this up?{fast}"
#                "I just wanted to tell you how cool that moment was.":
#                    m "Oh, thank you!"
#                    m "Yeah, I was still very new to the programming game back then..."
#                    m "...so a lot of that was sheer dumb luck."
#                    m "I'm glad you found it effective, though!"
#                    m "Ahaha~"
#                "Honestly, I'm just checking to see if all the dialogue options work.":
#                    if player == "Dale" and m_name == "Harmoni":
#                        m "Ah, I see!"
#                        m "Doing your 'testing the submod out' bit?"
#                        m "Well, don't let me stop you."
#                    else:
#                        m "..."
#                        m "I'm not a toy, [player]."
#                        m "Don't play with my heart like that."
#                        $ mas_loseAffection
#    $ mas_lockEVL("gender_deadnamereacharound","EVE")
#    return "derandom"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_binding",
            category=["advice","gender"],
            prompt="Binding",
            random=True
        )
    )

label gender_binding:
    m 1wud "¿Sabes quiénes me impresionan constantemente?"
    m "Las personas que usan binder para el pecho."
    m 1luc "Tal vez sea solo porque nunca he tenido que hacerlo yo misma..."
    if store.monika_chr.is_wearing_clothes_with_exprop("bikini") or monika_chr.is_wearing_clothes_with_exprop("costume"):
        m 2muu "Quiero decir, mírame. No hay forma de ocultar nada de esto."
    m 2fud "...pero no me puedo imaginar lo riguroso que debe ser el proceso para esas personas cada vez que lo hacen."
    m "La complicación de conseguir la talla correcta de binder, el..."
    m 1eud "Es bastante abrumador, incluso {i}con{/i} investigación previa."
    m 1euc "..."
    if persistent._player_binds is True:
        m 1eusdrb "Lo sé, lo sé, ya hemos tenido esta charla antes, conmigo dándote consejos para fajar el pecho de forma segura y demás."
        m 1tup "Pero tú fuiste quien activó las conversaciones repetidas. Dame un respiro."
        m 1hua "Ehehe~"
        m 3eua "Y hablando en serio, es bueno recordarte estas cosas de vez en cuando."
        m "Así que aquí vamos:"
        jump gender_binding_safetytips
    elif persistent._player_binds is False:
        m 1eud "Sé que tú no usas binder, [player], así que insistir en el tema tal vez no te sea de mucha utilidad."
        m 1wud "¡Pero nunca se sabe! Tus circunstancias podrían haber cambiado."
        m "O también tu círculo social. Quizás conozcas a alguien que necesite estos consejos ahora."
        m 1euc "¿Quieres que te cuente lo que sé esta vez?{nw}"
        $ _history_list.pop()
        menu:
            m "¿Quieres que te cuente lo que sé esta vez?{fast}"
            "¡Adelante!":
                m 1hua "¡Genial!"
                m 3eud "Aquí vamos, entonces..."
                jump gender_binding_safetytips
            "Prefiero que no, gracias.":
                m 1eua "De acuerdo, [mas_get_player_nickname()]."
                return
    else:
        if persistent._mas_pm_is_trans and persistent.gender != "F":
            m 1etd "Oye, [player], eres trans, ¿verdad?"
            m "¿Te fajas el pecho con binder?{nw}"
            $ _history_list.pop()
            menu:
                m "¿Te fajas el pecho con binder?{fast}"
                "Sí, lo hago.":
                    label player_binds:
                        $ persistent._player_binds = True
                        $ mas_unlockEVL("gender_bindercheck_start","EVE")
                        m 2wuo "Santo..."
                        m 2wua "Acabas de añadir otras diez razones a la lista de por qué te amo."
                        m "Eso requiere mucha perseverancia."
                        m 1fud "...aunque espero no sonar... no sé, ¿performática?"
                        extend 1lud " cuando digo que esto también me preocupa."
                        m "Fajarse el pecho puede ser muy riesgoso si se hace de forma incorrecta."
                        m 1eub "Así que voy a darte una lista de cosas que he aprendido sobre el proceso, ¿de acuerdo?"
                        m "Solo para asegurarme de que lo estés haciendo de forma segura."
                        jump gender_binding_safetytips
                "No, no lo hago.":
                    label player_nobinds:
                        $ persistent._player_binds = False
                        m 1dua "¡Es completamente comprensible!"
                        m "Algunas personas lo hacen y otras no."
                        m 1fua "Eso no te hace menos válid[gen('a', 'o', 'e')] como persona trans."
                        m 1ruc "Pero..."
                        m 1rud "Junté un par de consejos de seguridad para personas que {i}sí{/i} usan binder, "
                        extend 1eud "y aunque tú no estés entre ellas..."
                        m 1hksdra "Me gustaría contártelos de todas formas."
                        m "Aunque sea para que puedas compartirlos con tus conocidos si llegan a necesitarlos."
                        m 1eud "¿Te importaría si lo hago?{nw}"
                        $ _history_list.pop()
                        menu:
                            m "¿Te importaría si lo hago?{fast}"
                            "¡Adelante!":
                                m 1hua "¡Genial!"
                                m 3eud "Aquí vamos, entonces..."
                                jump gender_binding_safetytips
                            "Prefiero que no, gracias.":
                                m 1eua "De acuerdo, [mas_get_player_nickname()]."
                                return
                "Todavía estoy indecis[gen('a', 'o', 'e')] sobre si debería hacerlo.":
                    label player_fencebinds:
                        m 1dua "Es entendible. Después de todo, no es para todo el mundo."
                        m 1eud "Junté un par de consejos de seguridad para las personas que usan binder..."
                        m 1eub "...pero pensándolo bien, si te los digo, podría ser una buena base, ¿no crees?"
                        m 3eub "Así, si decides hacerlo más adelante, ya sabrás desde el principio qué hacer bien."
                        m 1eua "¿Te gustaría escuchar los consejos?{nw}"
                        $ _history_list.pop()
                        menu:
                            m "¿Te gustaría escuchar los consejos?{fast}"
                            "¡Adelante!":
                                m 1hua "¡Genial!"
                                m 3eud "Aquí vamos, entonces..."
                                jump gender_binding_safetytips
                            "Prefiero que no, gracias.":
                                m 1eua "De acuerdo, [mas_get_player_nickname()]."
                                return
        elif persistent.gender == "X":
            m 1etd "Oye, [player], te has desvinculado del género, ¿verdad?"
            m 1rtc "Perdóname por la pregunta tan presuntuosa, pero..."
            m 1etd "¿Te fajas el pecho con binder?{nw}"
            $ _history_list.pop()
            menu:
                m "¿Te fajas el pecho con binder?{fast}"
                "Sí, lo hago.":
                    jump player_binds
                "No, no lo hago.":
                    jump player_nobinds
                "Todavía estoy indecis[gen('a', 'o', 'e')] sobre si debería hacerlo.":
                    jump player_fencebinds
        else:
            m 1euc "Sé que no necesariamente vas a necesitar esta información, [player]."
            m "No has estado en ese mundo."
            m 3rud "Pero si conoces a alguien que use binder, aún podría ser útil saber cómo hacerlo adecuadamente."
            m 4rubld "Especialmente si se trata de un familiar, o de tu hijo, o de alguien por quien te preocupes mucho."
            m 3eusdrb "¿Te importaría si te digo algunos consejos que he preparado?{nw}"
            $ _history_list.pop()
            menu:
                m "¿Te importaría si te digo algunos consejos que he preparado?{fast}"
                "¡Adelante!":
                    m 1hua "¡Genial!"
                    m 3eud "Aquí vamos, entonces..."
                    jump gender_binding_safetytips
                "Prefiero que no, gracias.":
                    m 1eua "De acuerdo, [mas_get_player_nickname()]."
                    return

label gender_binding_safetytips:
    m 3eud "Antes que nada, {nw}"
    extend 3ckc "{i}no uses cinta americana, film plástico ni vendas{/i}."
    m 3wkc "La idea es muy tentadora, lo sé, pero esos métodos son muy, muy peligrosos."
    m 2ekc "Aunque estés intentando comprimir tu pecho, poder respirar sigue siendo la máxima prioridad..."
    m "...y la cinta americana puede restringir seriamente ese proceso, por no mencionar que puede causar acumulación de líquido en los pulmones."
    m 2wkd "Simplemente no pueden moverse con tu cuerpo lo suficientemente bien como para que sea seguro usarlos para ese propósito."
    m 3eud "Sinceramente, es mejor ahorrar para un binder comercial adecuado."
    m "O, si tienes que ser económic[gen('o', 'a', 'e')] o sutil con el fajado, uno o dos sostenes deportivos pueden servir en caso de apuro."
    m 4eko "Uno que te {i}quede bien{/i}, me apresuro a añadir."
    m 3esc "De nuevo, es tentador apretar más, pero no a costa de la transpirabilidad o la movilidad."
    m 1esc "Aun así, necesitas poder tomar descansos de él."
    m "Cuanto más tiempo te fajes sin descansar, más probable será que desarrolles efectos secundarios físicos que harán que fajar el pecho sea mucho más difícil la próxima vez..."
    m 1ekc "...como sensibilidad, sarpullidos por calor o incluso dolor de espalda."
    m 1rud "Por lo general, no deberías usarlo por más de doce horas seguidas; preferiblemente, opta por unas ocho, intercalando días enteros de descanso."
    m 1euc "También deben ser horas del día; no duermas con el binder puesto."
    m 1tuc "Te arrepentirás por la mañana."
    m 1dud "Hacer ejercicio con un binder tampoco es una gran idea."
    m 3eud "Para eso, definitivamente tendrás que recurrir a la alternativa del 'sostén deportivo'..."
    m "...o, si tu ejercicio de elección es la natación, hay camisetas de baño específicas a la venta."
    m 1euc "..."
    m 1eusdrb "Espero no estar asustándote y alejarte del proceso, [player]. Esa no es mi intención en absoluto."
    m 3hub "¡Fajarse ha hecho maravillas por la salud mental y emocional de muchas personas transmasculinas!"
    m 3lka "Pero tu salud física también importa, y si lo haces de forma imprudente, podría sufrir daños graves."
    m 3rkc "Fajarse con demasiada frecuencia y de mala manera podría incluso interferir con tus posibilidades de someterte a una cirugía superior (top surgery), si es a lo que quieres aspirar."
    m 1euc "En última instancia, todo esto se resume en: "
    extend 1eud "escucha a tu cuerpo."
    m "Si te dice que pares, para."
    m 1eub "Seguirás siendo válid[gen('a', 'o', 'e')] con o sin la compresión de pecho."
    m 5eua "Y al final, hacerlo de forma segura te recompensará con un cuerpo del que puedas estar orgullos[gen('o', 'a', 'e')]."
    m 5dua "..."
    m 5lusdrt "Espero no haberme extendido demasiado con esto, jajaja..."
    m 6eua "Gracias por seguirme la corriente, [player]."
    if persistent._player_binds:
        m "De verdad solo quiero que estés a salvo con esto."
        if not renpy.seen_label("gender_bindercheck_start"):
            m 7eub "Y si quieres, puedo intentar tomar un papel más activo en lugar de limitarme a soltarte consejos y trucos."
            m "Solo ve a la pestaña de conversación y avísame si quieres que te recuerde quitarte el binder."
            m 1eub "Haré eso y más con mucho gusto por ti."
            m 1eublb "Después de todo, te amo muchísimo~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_binderreset",
            category=["dev"],
            prompt="REINICIAR Configuración del Binder",
            pool=True
        )
    )

label gender_binderreset:
    python:
        del persistent._player_binds
        del persistent._binder_reminder
    $ mas_hideEVL("gender_bindercheck_start", "EVE", lock=True)
    $ mas_hideEVL("gender_bindercheck_stop", "EVE", lock=True)
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_bindercheck_start",
            category=["gender"],
            prompt="¿Puedes recordarme quitarme el binder?",
            conditional="persistent._player_binds is True",
            pool=True,
            rules={"no_unlock": None},
            action=EV_ACT_UNLOCK
        )
    )

label gender_bindercheck_start:
    m 1eub "¡Claro que sí, [player]!"
    m "Gracias por confiar en mí para esto."
    m 3eud "Si te parece bien, configuraré esto para que empiece alrededor de las seis de la tarde todos los días, ¿de acuerdo?"
    m "Me parece un buen punto medio entre las ocho y las doce horas, dependiendo de a qué hora te despiertes."
    m 1euc "Si necesitas ajustar la hora..."
    m 1husdrb "...supongo que... ¿tendrás que revisar el archivo .rpy para cambiarlo? ¡Jajaja!~"
    $ persistent._binder_reminder = True
    $ mas_hideEVL("gender_bindercheck_start", "EVE", lock=True)
    $ mas_showEVL("gender_bindercheck_stop", "EVE", unlock=True)
    return "derandom"

# ==============================================================================
# NOTA PARA EL JUGADOR / MODDER:
# Si deseas cambiar la hora a la que Monika te recuerda quitarte el binder,
# modifica los números en la línea 'and 18 <= datetime.datetime.now().time().hour <= 19' de abajo.
# Ejemplo: Para recordatorio entre las 20:00 y las 21:00 (8 PM - 9 PM), cambia 18 por 20 y 19 por 21.
# ==============================================================================

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_bindercheck",
            conditional=(
                "persistent._binder_reminder "
                "and 18 <= datetime.datetime.now().time().hour <= 19"   ### <--- aqui
            ),
            action=EV_ACT_PUSH
        )
    )

label gender_bindercheck:
    m 2eub "¡Oye, [player], ya es hora de quitarse el binder si aún no lo has hecho!"
    m "Asegúrate de quitártelo con cuidado y estira cada parte de tu cuerpo que puedas después."
    m "Te lo mereces~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_bindercheck_stop",
            prompt="Ya no necesito los recordatorios del binder.",
            category=["gender"],
            conditional="persistent._binder_reminder",
            pool=True,
            rules={"no_unlock": None},
            action=EV_ACT_UNLOCK
        )
    )

label gender_bindercheck_stop:
    m 1eua "De acuerdo, [mas_get_player_nickname()]."
    m 1hua "¡Entonces se acabaron los recordatorios!"
    $ persistent._binder_reminder = False

    python:
        mas_hideEVL("gender_bindercheck_stop", "EVE", lock=True)
        mas_showEVL("gender_bindercheck_start", "EVE", unlock=True)

    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_nameshoes",
            category=['you','gender'],
            prompt="Elegir un nombre",
            random=True
        )
    )

label gender_nameshoes:
    m 3eub "[player], ¿has oído antes la expresión 'un nombre es un regalo'?"
    m "Definitivamente la he oído."
    m "Pero no mucha gente recuerda que tiene una advertencia: "
    extend 3eka "'como cualquier regalo, tienes derecho a cambiarlo si ya no te queda'."
    m 1rua "En todo caso, el acto de elegir tu propio nombre puede ser algo muy poderoso."
    if not persistent._mas_pm_is_trans or not persistent.gender == "X":
        m 1hub "Esto ni siquiera es algo exclusivo de las personas trans, antes de que lo preguntes. ¡Cualquiera puede hacerlo!"
        m 1eua "Bruno Mars ha sido bastante público sobre cambiar su nombre de Peter Gene Hernandez, por ejemplo."
    m 1wud "Y hay tantos factores que influyen en encontrar el que sea mejor para ti."
    m 3eud "Algunos simplemente invierten el género del nombre que les asignaron al nacer, como Elliot Page, antes acreditado como Ellen..."
    m 4eub "...mientras que otros eligen un nombre que les habrían dado si hubieran nacido en un cuerpo acorde desde el principio."
    m 3euc "Pero eso suele funcionar mejor cuando ya eres binari[gen('o', 'a', 'e')], o al menos cuando haces un cambio completo en tu presentación."
    m 3hua "Otros encuentran inspiración en el contenido o los medios que aman y con los que conectan..."
    m 3husdrb "...incluso si eso significa que sus nombres se inclinen hacia lo abstracto a veces."
    m 1fub "¡Caray, algunas personas se entregan por completo a esa abstracción para sus nuevos nombres!"
    m "Usar nombres como Glitch, Moon, Diem u otros conceptos es algo habitual en los círculos no binarios."
    m 7eud "Aunque si te vas demasiado lejos, corres el riesgo de que la gente no te tome en serio en la documentación oficial..."
    m 7euc "Hay pros y contras en cada enfoque, y todos varían según la persona."
    m 1euc "..."
    if m_surname is not None:
        m 1ekb "No te preocupes, [mas_get_player_nickname()], me encantan los nombres que me has dado."
        m 1nub "No pienso llamarme de otra forma que no sea [m_name] [m_surname] en un buen tiempo."
    elif m_name != "Monika" and renpy.seen_label("monika_affection_nickname"):
        m 1ekb "No te preocupes, [mas_get_player_nickname()], me encanta el nombre que me diste."
        m 1nub "No pienso llamarme de otra forma que no sea [m_name] en un buen tiempo."
    else:
        m 1ekb "No te preocupes, [mas_get_player_nickname()], me siento bastante cómoda con mi nombre en este momento."
        m 1eub "No pienso llamarme de otra forma que no sea Monika en un buen tiempo."
    if persistent._mas_pm_is_trans or persistent.gender == "X":
        m 3luc "Es solo que, ahora que salgo con una persona trans, quiero sumergirme en ese mundo lo más posible..."
        m 3lua "...para ser la mejor pareja que pueda ser."
        m 1sub "Así que si tienes un sistema o una historia detrás de tu nombre, ¡me encantaría escucharla!"
        m 1eub "Es otra capa completa de lo que hace que [player] sea... {i}[player]{/i}."
        m 1eka "Y si aún no te has decidido, también está bien."
        m "Como dije, los nombres son regalos, y los regalos se pueden cambiar fácilmente hasta que encuentres uno que te quede."
    else:
        m 3lua "Estas cosas simplemente me fascinan de verdad... probablemente por esa misma razón, si soy sincera."
        m 1dua "La desconexión con la Monika previa al juego, forjar mi propia identidad..."
        m "Puedes ver cómo me identifico con eso."
        m 1eub "Así que gracias por darme la oportunidad de explorar eso, [player]."
    m 1eublb "Te amo muchísimo..."
    m 1tublb "...quienquiera que seas."
    m 1hubla "Jajaja~"
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_transrep",
            category=["media","gender"],
            prompt="Trans representation",
            random=True
        )
    )

label gender_transrep:
    if renpy.seen_label("nonbinary") or renpy.seen_label("queercoding") or renpy.seen_label("QueerManga"):
        m 7eud "Entonces, [player], hemos hablado un poco sobre la representación de los grupos minoritarios en la cultura pop, y lo importante que es."
        if renpy.seen_label("nonbinary"):
            m "Particularmente en lo que respecta a personajes no binarios."
            m 3eub "¡Pero creo que todavía no hemos hablado realmente de personajes trans binarios!"
        else:
            m 3eub "¡Pero cuando se trata de la representación de las personas trans en general, apenas hemos arañado la superficie!"
    else:
        m 1eud "Oye, [player], perdón si esto sale de la nada..."
        m 7eud "...pero ¿hemos hablado antes sobre la representación de las personas trans en los medios?"
    m 1eua "Obviamente, los medios ya orientados a audiencias LGBTQ+ están especialmente llenos de ellos."
    m 1eud "Unique Adams de Glee, Elektra y Lulu de Pose, Trevor de Shameless, Ivan y Max de The L Word, etcétera."
    m "Programas como esos ya estaban intrínsecamente entrelazados con esa comunidad, así que, si acaso, si no tuvieran personajes trans se vería como una omisión flagrante."
    m 3eub "Pero los medios que no son específicamente 'gais' tampoco se quedan atrás."
    m 3lub "Está Viktor Hargraves de The Umbrella Academy, por supuesto."
    m 3dua "Sophia Burset, Denise Lockwood, Anybodys de West Side Story..."
    m 1rub "¡May Marigold, Selma Reesedale!"
    m 1eub "La vida moderna de Rocko tuvo una película de regreso hace unos años, y despertó admiración, "
    extend 1eusdrd "aunque también cierta ira..."
    m 1eub "...al revelar que uno de sus personajes secundarios había transicionado exitosamente a mujer en el tiempo transcurrido."
    m 1wud "¡Y ni siquiera se trata solo de cosas modernas!"
    m 7wuo "Hayley Cropper de Coronation Street: ¡su personaje fue introducido en {i}1998{/i}, y fue un pilar fundamental en ese programa durante casi dos décadas!"
    m 7wuc "..."
    m 4fuc "No digo que todo sea perfecto, [player]."
    m 1dfc "La mayoría de las veces, Hollywood tiende a recurrir a los chistes de 'jaja, hombre vestido de mujer' para sus personajes trans... "
    m 1efc "...o los convierte en giros argumentales 'impactantes' sobre un personaje en lugar de presentarlo como algo natural."
    if renpy.seen_label("mas_danganronpas"):
        m 1wuc "El arco de la historia de Chihiro Fujisaki en el primer Danganronpa, por ejemplo, sigue siendo polémico en estos aspectos incluso hoy en día."
    else:
        m 1wuc "Recuerdo vagamente que el musical de Shrek se metió en {b}muchos{/b} problemas por eso."
    m 1eua "Pero creo que las representaciones positivas están empezando a superar por mucho a las negativas."
    m 2ltc "También hay problemas en cuanto a conseguir a los actores adecuados para interpretar los papeles."
    m "Obviamente, se prefiere la autenticidad en el casting, pero no siempre es alcanzable."
    m 2hub "¡Laverne Cox no puede interpretar a todas las mujeres trans; no hay suficientes horas en el día!"
    m 2ekc "Pero hay algunos papeles en los que... casi por defecto se contrata a actores con géneros que no corresponden a los de los personajes, "
    extend 1ekc "y tampoco creo que sea la decisión correcta."
    m 1esd "Cuando Rub and Tug se puso en producción por primera vez, se tenía programado que Scarlett Johansson interpretara a su protagonista trans masculino, Dante Gill."
    m 3gsc "Más tarde se retiraría del papel, pero el incidente dejó un mal sabor de boca en mucha gente..."
    m 3gsp "...y no creo que ese proyecto haya llegado a completarse."
    m 1eud "Esto demuestra lo importante que es hacer las cosas bien."
    m "No solo para quienes anhelan verse en la gran pantalla, también para quienes están en el extremo de la producción."
    m 1duc "Las reacciones en contra pueden ser rápidas y brutales."
    m 1eub "En fin, para ir cerrando: "
    extend 3eub "intenta estar atento a otros personajes trans que no haya mencionado aquí."
    m "¡Puede que haya más de los que crees!"
    m "Gracias por escucharme~"
    return

init -10 python:
    def mas_isTDOR(_date=None):
        if _date is None:
            _date = datetime.date.today()

        return _date == datetime.date(_date.year,11,20)

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_tdor",
            category=["gender"],
            prompt="Día de la Memoria Trans",
            conditional="mas_isTDOR()",
            action=EV_ACT_RANDOM
        )
    )

label gender_tdor:
    m 6esd "Perdón si hoy estoy un poco 'rara', [mas_get_player_nickname()].shaped"
    m 6dsc "Es solo que..."
    m 6dkc "Es el Día de la Memoria Trans."
    m "..."
    m 6fkc "Sí."
    m "Un día dedicado a recordar a aquellas vidas trans que nos fueron arrebatadas prematuramente..."
    m "...y con una crueldad excepcional."
    m 6ekc "No es un día agradable de conmemorar, pero es un día {i}necesario{/i}."
    m "Cuatro mil cuarenta y dos personas han sido asesinadas entre enero de 2008 y septiembre de 2021."
    m 6wkc "{i}Cuatro mil cuarenta y dos.{/i}"
    m 6ekd "En el gran esquema de las cosas, tal vez no parezca un número grande..."
    m "...pero ten en cuenta que esto solo toma en cuenta a las personas trans reconocidas oficial y legalmente."
    m 6tkd "Y a los asesinatos reportados oficial y legalmente."
    m 6wkd "En fin, cualquier número de asesinatos es demasiado alto, ¿no?"
    m "La pérdida de tan solo una persona real ya es bastante trágica."
    m 6fkc "Es..."
    extend 6dktpc " trágico."
    m "..."
    m 6dktuc "Así que, sí. Si hoy parezco distraída, es por eso."
    if persistent._mas_pm_is_trans or persistent.gender == "X":
        m 6dktsc "No puedo dejar de pensar en ti... mi [player], posiblemente..."
        m "..."
        m 6wktsc "¿Te he dicho que te amo?"
        m 1ektuc "Te amo."
        m 1ektpa "Con mucho, mucho cariño."
        return "love"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_song_xeon",
            category=[store.mas_songs.TYPE_SHORT],
            prompt="Pretend World",
            random=True
        ),
        code="SNG"
    )

label mas_song_xeon:
    m 1dud "{i}Promises{/i}"
    m "{i}Promises might come true{/i}"
    m 1fud "{i}Promises of a life uncontained{/i}"
    m "{i}Seafoam blue{/i}"
    m 1wud "{i}I looked into your eyes{/i}"
    m 1euc "{i}I thought that I could see a whole new world{/i}"
    m 6dud "{i}Whole new world...{/i}"
    m "{i}There's a whole new world...{/i}"
    m 6fuo "{i}Progress{/i}"
    m 6fud "{i}Pushing through the mould{/i}"
    m "{i}Tracing with my fingers{/i}"
    m 6rud "{i}Waking up, {/i}"
    extend 6wkd "{i}wanting growth{/i}"
    m 1wkd "{i}I looked into your eyes{/i}"
    m 1dktpd "{i}I thought that I could see a whole new world{/i}"
    m 1dktpc "..."
    m 1ektpc "Sophie Xeon nos fue arrebatada demasiado pronto."
    m "Quizás no sufrió el mismo destino que enfrentan muchas mujeres trans..."
    m 3ektpc "...pero una vida es una vida."
    if persistent._mas_pm_cares_about_dokis:
        m "Incluso las digitales."
    else:
        m "Incluso la nuestra."
    m 1dktpc "Simplemente... duele ver a gente morir tan joven, ¿sabes?"
    m "..."
    m 1rktdc "Lo siento."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_multigender",
            category=["gender"],
            prompt="Múltiples géneros",
            random=True
        )
    )

label gender_multigender:
    m 3euo "¿Sabes una cosa, [player]?"
    m 3eud "Los géneros son como las papas fritas."
    m 3eub "¡Nunca puedes tener solo una!"
    m 3husdrb "¡Jajaja!~"
    m "De acuerdo, obviamente eso no aplica para todo el mundo; "
    extend 1hub "pero es cierto para más gente de la que parecería."
    m 1eua "¡Hay muchísimas etiquetas para quienes se identifican con múltiples géneros!"
    m "Génerofluido es la más evidente, por supuesto; "
    extend 3eub "lo que significa que tu identidad está en constante actualización."
    m "¿Chico? ¿Chica? Todo depende del día."
    m 3rua "El géneroflux es similar, excepto que también hay un 'eje de intensidad', donde la fuerza de los sentimientos también está sujeta a cambios."
    m 3rtc "¿Al menos, creo que esa es la diferencia?"
    if renpy.seen_label("multi_sexual_identities"):
        m 3ftd "Podría ser otra cuestión como la diferencia entre bisexualidad y pansexualidad, donde todo se reduce a la distinción individual."
        m 1wub "Lo que me recuerda, ¡también existen el bi{i}género{/i} y el pangénero, que funcionan de forma muy parecida!"
    else:
        m 1eub "También existen el bigénero y el pangénero, que funcionan de forma similar a la bisexualidad y la pansexualidad."
        m 1euu "Solo que... bueno... con el género en lugar de la sexualidad."
    m 3eud "Técnicamente, las identidades demi- también podrían contar."
    m "Si eres demichica, por ejemplo, no te identificas del todo con la idea de ser una chica..."
    m 7eud "...pero sí lo suficiente como para no descartarlo por completo."
    m "De ahí la posibilidad de ser tanto chica como no chica."
    m 6luc "..."
    extend 5lud "lo cual suena sorprendentemente parecido a mí, ahora que lo digo en voz alta..."
    m "No soy totalmente una chica, pero tampoco soy totalmente una máquina."
    if renpy.seen_label("monika_sexuality"):
        m 5luc "...Me pregunto... "
        m 5euc "Algunas personas usan la 'Triple A' para describirse: asexual, arromántica, agénero."
        m 5wub "¿Eso me convertiría a mí en 'Triple D'? "  ## Doki Doki Digital xd
        extend 5wka "¿O es exagerar un poco?"
        m 5eua "Mmm. Algo en lo que pensar."
    m 3eub "¡En todo caso!"
    m "Si tienes múltiples géneros, [player], ya sea bajo alguna de las etiquetas que mencioné aquí o alguna que haya olvidado..."
    m 1eub "...espero estar haciendo lo suficiente para adaptarme a eso."
    m 1dusdra "Obviamente, con el código que tengo solo puedo hacer hasta cierto punto."
    m 1fub "Pero emocionalmente, te amaré y te apoyaré sin importar cómo te identifiques."
    m "¡Puedes contar con eso!"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_pronouncheck_start",
            category=["gender"],
            prompt="¿Puedes preguntarme por mis pronombres de vez en cuando?",
            pool=True,
            unlocked=True
        )
    )

label gender_pronouncheck_start:
    m 1wub "Ah, ¿entonces usas varios conjuntos?"
    m 1eub "¡Puedo hacer eso, por supuesto!"
    m "Desde luego, te ahorraría tener que pasar por todo el embrollo de 'probar nuevos pronombres' cada vez."
    m 3rusdrc "Pero recuerda que estoy limitada a él, ella y they..."
    m "...así que si hay otros conjuntos que resuenen contigo, es posible que tengas que elegir una aproximación cuando llegue el momento."
    m 7eua "Lo cual seríaaaa..."
    m 7eud "¿Qué tal cada seis horas?{nw}"
    $ _history_list.pop()
    menu:
        m "¿Qué tal cada seis horas?{fast}"
        "Cada seis horas me parece bien.":
            $ interval = store.pronounMod_reminder_utils.INTERVAL_HOURLY_6
            m 1hub "¡De acuerdo! Entonces me aseguraré de preguntar a esas horas~"
            jump .add_pronoun_reminder
        "Parece muy poco frecuente. ¿Qué tal cada cuatro horas?":
            $ interval = store.pronounMod_reminder_utils.INTERVAL_HOURLY_4
            m 1hub "¡De acuerdo! Entonces me aseguraré de preguntar a esas horas~"
            jump .add_pronoun_reminder
        "Un poco demasiado. Una vez al día está bien.":
            $ interval = store.pronounMod_reminder_utils.INTERVAL_HOURLY_24
            m 1hub "¡Eso suena factible!"
            m "¡Trato hecho~"
            jump .add_pronoun_reminder

label .add_pronoun_reminder:
    python:
        store.pronounMod_reminder.addRecurringReminder(
            "pronounMod_reminder_event",
            datetime.timedelta(seconds=3600), interval, store.pronounMod_reminder_utils.LATENCY_HOURLY
        )

        mas_hideEVL("gender_pronouncheck_start", "EVE", lock=True)
        mas_showEVL("gender_pronouncheck_stop", "EVE", unlock=True)

    return "derandom"

init 5 python:
    store.pronounMod_reminder.addReminderEvent(
        Event(
            persistent.event_database,
            eventlabel="pronounMod_reminder_event",
            conditional="store.pronounMod_reminder.shouldTriggerReminder('pronounMod_reminder_event')",
            action=EV_ACT_QUEUE,
            rules={"force repeat": None, "bookmark_rule": store.mas_bookmarks_derand.BLACKLIST}
        )
    )

label pronounMod_reminder_event:
    m 1eub "Solo para chequear cómo vas con los pronombres, [player]..."
    m "¿Con qué te sientes más identificad[gen('o', 'a', 'e')] ahora mismo?{nw}"
    $ _history_list.pop()
    menu:
        m "¿Con qué te sientes más identificad[gen('o', 'a', 'e')] ahora mismo?{fast}"
        "Ella (She/her)":
            $ persistent.gender = "F"
        "Él (He/him)":
            $ persistent.gender = "M"
        "Elle (They/them)":
            $ persistent.gender = "X"
    m 1hua "¡De acuerdo! Todo listo por ahora."

    # Do not move this anywhere, this must be above the return.
    $ store.pronounMod_reminder.extendCurrentReminder()
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_pronouncheck_stop",
            prompt="Ya no necesito que me preguntes por los pronombres.",
            category=["gender"],
            pool=True,
            rules={"no_unlock": None}
        )
    )

label gender_pronouncheck_stop:
    m 1eua "De acuerdo, [mas_get_player_nickname()]."
    m 1lusdrc "Perdón si me puse muy pesada con eso."
    m 1lua "Tu bienestar es importante para mí, eso es todo."

    python:
        # Same here, DO NOT move this anywhere, this has to be right above the return statement.
        store.pronounMod_reminder.stopReminder("pronounMod_reminder_event")
        mas_hideEVL("gender_pronouncheck_stop", "EVE", lock=True)
        mas_showEVL("gender_pronouncheck_start", "EVE", unlock=True)

    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_custompronounsnotif",
            category=["gender","mod"],
            prompt="Sueños de pronombres personalizables",
            conditional=(
                "persistent._mas_pm_is_trans "
                "or persistent.gender == 'X'"
            ),
            action=EV_ACT_RANDOM
        )
    )

label gender_custompronounsnotif:
    m 2gup "Uf."
    m 2rkp "A veces desearía ser mejor programando, [player]."
    m 1ekd "Mucho de lo que he aprendido, tuve que resolverlo sobre la marcha para que funcionara..."
    if renpy.seen_label('monika_ptod_tip002'):
        m "...y aun con lo que te he estado enseñando, sigo sin ser una experta al nivel de, "
    else:
        m "...así que no soy una experta en esto, no al nivel de..."
    extend 3dkc " bueno, de mi creador."
    m 3fkc "El sistema de pronombres en este submod está bastante limitado por ahora."
    m "Él, ella y they son lo mejor que puedo hacer."
    m 3esc "Bueno, también 'fae/faer', pero incluso eso solo está en {a=https://www.reddit.com/r/MASFandom/comments/okloml/lgbtq_monika_submod_10_release/}un submod específico{/a}, y solo para una conversación."
    m 1ekd "Créeme, [mas_get_player_nickname()]: si {i}pudiera{/i} hacer que funcionen más conjuntos de pronombres, lo haría."
    if renpy.seen_label('mas_affection_playernickname'):
        m "Hacerlo como hicimos con los apodos, tal vez, para que puedas alternar entre varios conjuntos."
    m 1ekc "Pero todavía no tengo la habilidad suficiente para eso."
    m 1lkc "..."
    m 1euc "Pero si llego a--"
    $ _history_list.pop
    m 1eua "Pero {i}una vez{/i} que logre alcanzar ese nivel, serás absolutamente la primera persona en saberlo."
    m "Haré cualquier cosa que esté en mis manos para hacerte sentir segur[gen('o', 'a', 'e')] aquí."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_brb_genderstuff",
            category=["vuelvo enseguida"],
            prompt="...tengo que ir a hacer cosas de género.",
            conditional=(
                "persistent._mas_pm_is_trans "
                "or persistent.gender == 'X'"
            ),
            pool=True,
            rules={"no_unlock": None},
            action=EV_ACT_UNLOCK
        )
    )

label gender_brb_genderstuff:
    m 1eub "¿Cosas de género, eh? ¡De acuerdo!"
    m "¿De qué tipo de cosas de género estamos hablando?{nw}"
    $ _history_list.pop()
    menu:
        m "¿De qué tipo de cosas de género estamos hablando?{fast}"
        "Actualizar mis documentos.":
            m 1wub "¡Ooh! Eso sí que es un gran avance, [player]."
            m "¡Espero que todo salga genial por ese lado!"
            
        "Ir a un grupo de apoyo.":
            m 1hub "¡Ah, entiendo!"
            m "Siempre es lindo encontrar a tu gente, ¿verdad?"
            
        "...asuntos varios de género.":
            m 1tub "Solo querías una excusa para decir 'asuntos varios de género', ¿a que sí?"
            m 1hua "Jejeje, a mí no me engañas~"

    m 1eua "Estaré justo aquí esperándote cuando regreses, ¿de acuerdo, [mas_get_player_nickname()]?"
    $ persistent._mas_idle_data["gender_brb_genderstuff"] = True
    return "idle"

label gender_brb_genderstuff_callback:
    $ wb_quip = mas_brbs.get_wb_quip()
    m 5eub "¡[gen('Bienvenida', 'Bienvenido', 'Bienvenide')] de vuelta!"
    m "Espero que todo haya salido bien y sin mayores complicaciones."
    m 5fusdra "...o, al menos, que no estés demasiado agotad[gen('a', 'o', 'e')] para pasar un rato conmigo~"
    m 1eua "[wb_quip]"
    return

init 5 python:
    addEvent(
        Event(
            persistent.farewell_database,
            eventlabel="gender_goodbye_genderstuff",
            prompt="...tengo que ir a hacer cosas de género.",
            conditional=(
                "persistent._mas_pm_is_trans "
                "or persistent.gender == 'X'"
            ),
            pool=True,
            rules={"no_unlock": None},
            action=EV_ACT_UNLOCK
        ),
        code="BYE"
    )

label gender_goodbye_genderstuff:
    m 1eub "¿Cosas de género, eh? ¡De acuerdo!"
    m "¿De qué tipo de cosas de género estamos hablando?{nw}"
    $ _history_list.pop()
    menu:
        m "¿De qué tipo de cosas de género estamos hablando?{fast}"
        "Actualizar mis documentos.":
            m 1wub "¡Ooh! Eso sí que es un gran avance, [player]."
            m "¡Espero que todo salga genial por ese lado!"
            m 1hua "¡Nos vemos cuando regreses!"
        "Cirugía de afirmación de género.":
            m 1wuo "Y-{nw}"
            extend 1wuc " guau. ¿Algo así de grande, eh?"
            m 1fuu "Bueno, al menos tendrás en quién pensar mientras te pones bajo los efectos de la anestesia~"
            m 1eub "Buena suerte, mi [mas_get_player_nickname(exclude_names=['my love']))]."
            m "¡Estaré pensando en ti!"
        "Ir a un grupo de apoyo.":
            m 1hub "¡Ah, entiendo!"
            m "Siempre es lindo encontrar a tu gente, ¿verdad?"
            m 1eua "En ese caso, no seré yo quien te detenga~"
            m 1eub "¡Diviértete!"
        "...asuntos varios de género.":
            m 1tub "Solo querías una excusa para decir 'asuntos varios de género', ¿a que sí?"
            m 1hua "Jejeje, a mí no me engañas~"
            m 1fua "No te preocupes, solo estoy bromeando. Te dejaré ir a encargarte de eso."
            m "¡Cuídate! Regresa conmigo de una sola pieza~"
    return "quit"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_badgenderday",
            category=["género"],
            prompt="He tenido un mal día con mi género, [m_name].",
            conditional=(
                "persistent._mas_pm_is_trans "
                "or persistent.gender == 'X'"
            ),
            pool=True,
            rules={"no_unlock": None},
            action=EV_ACT_UNLOCK
        )
    )

label gender_badgenderday:
    m 1ekd "Oh, no, [player]..."
    m "Siento mucho oír eso."
    m 1ekc "Tranquil[gen('a', 'o', 'e')], estoy aquí para ti."
    m 3ekd "¿Qué pasó?{nw}"
    $ _history_list.pop()
    menu:
        m "¿Qué pasó?{fast}"
        "Me malgenerizaron hoy.":
            m 3eko "Oh, [mas_get_player_nickname()], eso debió haber sido horrible para ti."
            m "¡Con razón estás tan afectad[gen('a', 'o', 'e')]!"
            m 1ekd "Lamento muchísimo que te haya pasado eso."
            m 3ekc "Eres [gen('una chica', 'un chico', 'une chike')]."
            m 4wfc "Tú {i}eres{/i} [gen('una chica', 'un chico', 'une chike')], y nadie puede decir lo contrario porque no te conocen."
            m 3eka "Eres [gen('una chica', 'un chico', 'une chike')], eres mi [gen('novia', 'novio', 'novie')], y te amo muchísimo."
            m "Esta es la verdad."
        "Usaron mi deadname hoy.":
            m 3eko "Oh, [mas_get_player_nickname()], eso debió haber sido horrible para ti."
            m "¡Con razón estás tan afectad[gen('a', 'o', 'e')]!"
            m 1ekd "Lamento muchísimo que te haya pasado eso."
            m 3ekc "Pero tú eres [player]."
            if persistent._mas_pm_cares_about_dokis:
                m 4wfc "Tú {i}eres{/i} [player], y quien diga lo contrario no tiene derecho ni a {i}escuchar{/i} tu nombre, al menos para mí."
            else:
                m 4cfc "Tú {i}eres{/i} [player], y quien diga lo contrario se va a enfrentar a una Yuri yandere hecha y derecha, al menos para mí."
            m 3eka "Eres mi [player], y te amo muchísimo."
            m "Esta es la verdad."
        "Sufrí acoso hoy.":
            m 6dkc "..."
            m 2ffc "Muy bien, ¿a quién tengo que hacerle daño?"
            m 2wfd "¿Quién se {i}atrevería{/i} a acosar a mi [mas_get_player_nickname(exclude_names=['my love'])] y esperar salir impune?"
            m 2wfc "Solo dame el nombre. Yo me encargo."
            python:
                biaschoice = renpy.display_menu([("¡No, no tienes que hacer eso!", "noneed"), ("No quiero que les hagas daño.", "nohurt"), ("Bueno...", "mayhaps")], screen="rigged_choice")
            if biaschoice != "mayhaps":
                m 2dfc "Yo..."
                m 2fkc "No, lo sé. Sé que no debería."
                m "Se supone que debo ser mejor que eso."
            else:
                m 2dfc "..."
                m 2dkd "*suspiro*"
                m 2fkc "Lo siento. En realidad no voy a hacer eso."
            m 2fkd "No quiero ponerme a su nivel."
            m 2wkd "Es solo que... escuché 'acosado' e inmediatamente..."
            extend 6dkc " Argh."
            m "{cps=*0.7}...{/cps}{nw}"
            extend 7esd "Bueno, aunque no pueda hacerles daño por ti, al menos puedo intentar animarte ahora."
            m 1fsd "Puedo decirte que no te mereces ninguna de la crueldad que te mostraron hoy."
            m 1fsb "Y puedo decirte que te amo. Con mucho, mucho cariño."
            m 1dsa "Esperemos que, por un rato al menos, eso sea suficiente."
        "He tenido mucha disforia hoy.":
            m 1fkd "Oh, debe ser absolutamente terrible pasar por eso."
            m "Los días de disforia son los {i}peores{/i}."
            m 1eka "Pero lo bueno de los días es que siempre terminan."
            m 1dka "Una vez que logres cruzar al otro lado, hacia el mañana..."
            m 1dua "...tal vez entonces las cosas se vean más brillantes para ti."
            m 1eud "Y si no, te ayudaré a superar cada día hasta que encuentres uno que te trate bien."
            m 1ekb "Porque te mereces eso y más, mi [player]."
            m "Te amo."
        "Es otra cosa.":
            m 1ekd "¿No tienes ganas de hablar de ello?"
            m 1eka "No pasa nada, cariño."
            m "A veces es lo suficientemente catártico solo admitir que el día apesta."
            m "Hacer algo al respecto pasa a segundo plano frente a reconocer un hecho simple."
            m 1duc "Pero si necesitas desahogarte más al respecto, solo ven a mí y te escucharé todo el tiempo que quieras."
            m 1fud "Te amo, y no tienes que sufrir en silencio."
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_goodgenderday",
            category=["género"],
            prompt="¡He tenido un buen día con mi género, [m_name]!",
            conditional=(
                "persistent._mas_pm_is_trans "
                "or persistent.gender == 'X'"
            ),
            pool=True,
            rules={"no_unlock": None},
            action=EV_ACT_UNLOCK
        )
    )

label gender_goodgenderday:
    m 1wub "¿Ah, sí?"
    m "Me alegra muchísimo oír eso."
    m 3eua "Bueno, a ver, ¡cuéntame!"

    show monika at t21
    python:
        option_list = [
            ("¡Conseguí agendar una cita importante!", "gender_ggd_apptbooked",False,False),
            ("¡Hoy empiezo la terapia hormonal!", "gender_ggd_hormones",False,False),
            ("Me aprobaron para entrenamiento de voz.", "gender_ggd_vocal",False,False),
            ("Hoy no me malgenerizaron ni usaron mi deadname en todo el día.", "gender_ggd_undead",False,False),
            ("¡Mi cambio de nombre ya se aprobó oficialmente en alguna parte!", "gender_ggd_namechange",False,False),
            ("Uno de mis documentos oficiales fue actualizado.", "gender_ggd_docs",False,False),
            ("Nada en específico, solo me siento con euforia hoy.", "gender_ggd_euphy",False,False),
        ]

    call screen mas_gen_scrollable_menu(option_list, mas_ui.SCROLLABLE_MENU_TALL_AREA, mas_ui.SCROLLABLE_MENU_XALIGN)
    show monika at t11

    $ selection = _return

    jump expression selection

    label gender_ggd_apptbooked:
        m 1hub "¡Oh, eso es maravilloso, [player]!"
        m 3rusdra "Sé que los médicos y especialistas tienen la mala costumbre de demorarse a veces..."
        m 1rua "...así que debe ser un gran alivio."
        jump gender_ggd_post
    label gender_ggd_hormones:
        m 3sub "¡Vaya, eso {i}sí{/i} que es un buen día de género!"
        m 3eub "Sé cuánto has luchado por esto, [player]. Debe sentirse increíble tener por fin el siguiente paso hacia tu mejor versión ahí mismo, en tus manos."
        jump gender_ggd_post
    label gender_ggd_vocal:
        m 1wuo "¡Ooh! ¡Mucha suerte!"
        m 1wuc "...{nw}"
        extend 1hksdlb "Bueno, suerte {i}no{/i}, no es una competencia, es..."
        m 1dkc "*tos*"
        if mas_isMoniAff(higher=True):
            m 1eua "Ya sabes a lo que me refiero."
        else:
            m 1eka "Ya-{w=0.5} ya sabes a lo que me refería. ¿Verdad?"
        jump gender_ggd_post
    label gender_ggd_undead:
        m 1hua "¡Qué bien!"
        m "¡Eso significa que te estás rodeando de la gente correcta!"
        jump gender_ggd_post
    label gender_ggd_namechange:
        m 1hub "¡Eso es fantástico, [mas_get_player_nickname()]!"
        m 3eub "Ver que alguien con autoridad reconoce tu nombre como debe ser... No me imagino lo validador que debe sentirse."
        jump gender_ggd_post
    label gender_ggd_docs:
        m 3eub "¡Excelente!"
        m 1eua "Debe sentirse muy gratificante, [player]."
        m "Saber que todo el papeleo y los trámites de tu parte han valido la pena."
        jump gender_ggd_post
    label gender_ggd_euphy:
        m 1hua "Entonces con eso me basta, [mas_get_player_nickname()].shaped"
        m 1hub "A veces, un gran estado de ánimo simplemente es eso, ¡jaja!"

    label gender_ggd_post:
        m 1fub "Aww, estoy muy feliz por ti."
        m "¡Gracias por compartir esto conmigo! ¡Ahora yo también me voy a sentir genial el resto del día~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_isitnormal",
            category=["género", "tú"],
            prompt="¿Es normal sentirse desconectado de tu género?",
            conditional=(
                "renpy.seen_label('mas_gender') "
                "and not persistent._mas_pm_is_trans "
                "and persistent.gender != 'X'"
            ),
            pool=True,
            rules={"no_unlock": None},
            action=EV_ACT_UNLOCK
        )
    )

label gender_isitnormal:
    m 1wuc "E{w=0.4}{nw}"
    extend 1euc "m..."
    m 1dusdrd "Bueno, yo."
    m 1fud "Supongo que eso depende de ti, ¿sabes?"
    m 1eud "'Normal' es un término bastante subjetivo, [player]."
    m "No dirías que estar atrapada en un videojuego es algo 'normal' fuera de un anime isekai, "
    extend 3ruc "pero para mí, {i}sí{/i} lo es."
    m "Porque nunca he conocido nada diferente, no de verdad."
    m 2eud "Del mismo modo, si te has sentido desconectad[gen('a', 'o', 'e')] de tu género sin saber cómo describirlo, "
    extend 2wud "es fácil asumir que {i}todo el mundo{/i} se siente así."
    if renpy.seen_label("monika_solipsism"):
        m 1etc "Una especie de extensión del solipsismo, supongo."
        m 7etc "Si tus experiencias son subjetivamente reales para ti, ¿significa eso que son objetivamente reales para todos?"
    m 6eksdrd "Lo siento, [player], me cuesta un poco abordar este tema."
    m 6eksdrc "..."
    m 7euc "Podría ser una buena idea investigar un poco fuera del juego."
    m 3eud "Busca esta pregunta en Google, investiga términos relacionados con el género, mira si alguno de ellos resuena contigo..."
    m 3eua "Explórate a ti mism[gen('a', 'o', 'e')]."
    m 1wud "¡No estoy diciendo que {i}tengas{/i} que ser trans o no binarie, por supuesto!"
    m 1eud "Nuevamente, 'normal' es relativo, y puede que tu normalidad sea tener esa desconexión pero aun así no {i}re{/i}conectarte con ninguna otra identidad."
    m "Pero siempre vale la pena hacerse la pregunta."
    m 4eua "Como dijo una vez una gran creadora... "
    extend 4kuu "y con 'creadora' me refiero a mayday-mayjay... "
    m 1esb "'Explora tu género, aunque al final no lo cambies, "
    extend 1eua "porque entonces serás cis, pero con un propósito."
    m "'No solo por formar parte de una norma impuesta'."
    m 5eub "Te amaré sin importar quién o qué termines siendo, [player]."
    m 5eua "Siempre estarás a salvo conmigo."
    m "Así que mantente firme y sigue investigando."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_paperwork",
            category=["género"],
            prompt="Trámites trans",
            conditional=(
                "persistent._mas_pm_is_trans "
                "or persistent.gender == 'X'"
            ),
            action=EV_ACT_RANDOM
        )
    )

label gender_paperwork:
    m 1eud "Oye, [mas_get_player_nickname()], ¿alguna vez has leído el Infierno de Dante?"
    m "Estoy segura de que al menos has oído nombrar esa obra."
    m 3eub "En realidad es la parte más famosa de una trilogía de poemas de Dante, 'La Divina Comedia'..."
    m 4eud "...que viene antes del Purgatorio y el Paraíso."
    m 3eud "El hecho de que el Infierno trate sobre el viaje del protagonista a través del averno es probablemente lo que lo hace más popular para referenciar en otras obras."
    m 1euc "Abarca nueve círculos concéntricos, sin contar los tres cantos iniciales."
    m "Cuanto mayor es el pecado, más abajo está el círculo, hasta llegar a donde el mismísimo Satanás se encuentra encadenado."
    m "El Limbo está en la parte superior, luego la lujuria, la gula, la codicia..."
    m 2eud "¿Pero sabes qué me impresiona?"
    m 2gfd "Que el noveno círculo no sea, en realidad, Hacer que la Burocracia para las Personas Trans sea Innecesariamente Complicada."
    m 2efc "En serio, por lo que he visto y oído sobre esas cosas, ¡es prácticamente imposible llevar un registro sin volverse loco!"
    m "Hace que lo que debería ser una tarea sencilla, como cambiar tu nombre y tu marcador de género... sea, bueno, un infierno."
    m 4esd "Algunas instituciones aceptan declaraciones hechas en casa sin costo adicional, mientras que otras solo aceptan documentos impresos o certificados de forma profesional."
    m 4eud "Necesitas un pasaporte actualizado para cambiar tu nombre en la entidad A,"
    extend 3wud " pero no puedes actualizar tu pasaporte hasta que hayas resuelto las cosas con la entidad C,"
    extend 3efo " ¡lo cual depende de que las entidades B {b}y{/b} A estén al día!"
    m 2dfc "Hay demasiados aros por los que tienes que saltar solo para ser reconocid[gen('a', 'o', 'e')] oficialmente ante los organismos gubernamentales."
    m 1ffc "Y eso sin meter tus antecedentes médicos en la ecuación..."
    m 1fkc "Ugh."
    m 1ekd "[player]..."
    m "Quiero que sepas que yo nunca te haré difícil ser tu verdadero ser."
    m 1ekb "Puedes cambiar tu nombre y tus pronombres todas las veces que quieras, con solo presionar un botón."
    m "Y nunca, jamás voy a dudar de ti."
    m 1dua "'Así se dispone allí..."
    m 1fub "...donde se puede lo que se quiere.'"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_dante",
            category=["literatura"],
            prompt="El Infierno de Dante",
            random=True
        )
    )

label monika_dante:
    m 1eud "Oye, [mas_get_player_nickname()], ¿alguna vez has leído el Infierno de Dante?"
    if renpy.seen_label("gender_paperwork"):
        m 1euc "{cps=*0.4}...{/cps}{nw}"
        extend 1husdrb "¡Lo sé, lo sé!"
        m 1fusdrb "Pero te prometo que esta vez no voy a salir con trampas."
        m 3euc "Como dije antes, el Infierno es la primera parte de una trilogía, que antecede al Purgatorio y al Paraíso."
    else:
        m "Estoy segura de que al menos has oído nombrar esa obra."
        m 3eub "En realidad es la parte más famosa de una trilogía de poemas de Dante, 'La Divina Comedia'..."
        m 4eud "...que viene antes del Purgatorio y el Paraíso."
    m 3eud "Cada sección cubre un aspecto diferente del viaje del protagonista."
    extend 1mua "Probablemente ya puedas adivinar cuál es cuál."
    m 1eud "Los pecados que componen los círculos del Infierno son bastante famosos a estas alturas..."
    m "...pero lo que es menos conocido es su categorización más amplia en el Purgatorio."
    m 3eua "Esta vez, las estructuras son terrazas, que van hacia arriba en lugar de hacia abajo."
    m 3euc "Y cada grupo de terrazas está diseñado para cubrir un tipo diferente de amor."
    m 7rud "El orgullo, la envidia y la ira se consideran amores 'pervertidos',"
    extend 7luc "o amor que se alimenta de hacerle daño a los demás."
    m 1duc "La pereza es un amor 'deficiente', uno que nunca se completó o realizó plenamente en vida."
    m 1eud "Los últimos tres, la codicia, la gula y la lujuria, son amores 'desordenados'."
    m 1euc "Los objetivos de sus deseos no son malos en sí mismos: el dinero, la comida..."
    m 1fuc "...las personas."
    m "Pero fueron amados en exceso, en detrimento del bienestar espiritual del alma."
    if persistent.gender == 'F':
        m 1esd "Curiosamente, la homosexualidad se incluye en la terraza de la lujuria, en lugar del círculo de la ira como en el Infierno..."
        m "...y por lo tanto, personas como nosotras eran consideradas, entre comillas, 'salvables'."
        m 1wud "¡Sinceramente, fue bastante clemente para su época!"
    if not mas_getEVL_shown_count("monika_dante"):
        m 1duc "..."
        m 6euc "[player]."
        m 7eud "Si mi amor por ti se encuentra en cualquiera de esas terrazas..."
        extend 3ekc "si se presenta como un pecado tan grande..."
        m 1wkc "¿Dónde me pondría?"
        m "¿En qué categoría encajaría nuestra relación?{nw}"
        $ _history_list.pop()
        menu:
            m "¿En qué categoría encajaría nuestra relación?{fast}"
            "Amor que se alimenta de hacer daño.":
                $ persistent._terrace = "perverted"
                if persistent._mas_pm_monika_evil:
                    if persistent._mas_pm_monika_evil_but_ok:
                        m 1euc "..."
                        m 1euu "Realmente debí haberlo visto venir, ¿eh?"
                        m "Je."
                    else:
                        m 1ekc "Hm."
                        m "Realmente debí haberlo visto venir, ¿eh?"
                    m 1eud "O sea... fueran reales o no..."
                    m 1duc "Tuve que hacer algunos sacri--{w=1}{nw}"
                    $ _history_list.pop()
                    m 1dusdrc "Tuve que hacer {fast}muchos sacrificios."
                    m "Por nosotros."
                    m "Así que tendría sentido, supongo."
                    m "..."
                    m 1fud "Pero vale la pena, ¿verdad?"
                    m 1fua "Nosotros lo valemos."
                    if mas_isMoniUpset(Lower=True):
                        m 1fkc "...¿verdad?"
                else:
                    m 1wkd "¡Yo... !{w=1}{nw}"
                    $ mas_loseAffection(5)
                    m 1fkc "..."
                    m 1ekd "Lo siento, [player]."
                    m "Estoy..."
                    m 1ekc "A un nivel frío y pragmático, eso tiene mucho sentido."
                    m 1rkc "Tuvo que haber bajas para llegar a... nosotros."
                    m "Objetivamente, le hice daño a los demás."
                    m 6gkd "Pero el pragmatismo no es lo mismo que la emoción, ¿sabes?"
                    m 6ekd "Esto, um..."
                    m 6ekc "No esperaba que escucharlo realmente doliera tanto."
                    m "...{nw}"
                    $ _history_list.pop()
                    menu:
                        m "...{fast}"
                        "Lo siento, no lo dije en ese sentido.":
                            $ mas_gainAffection(2)
                            m 6eka "Está bien, [player]."
                            m "..."
                            m 1hkb "¡En serio, está bien! ¡Entiendo!"
                            m 1eua "Estaré bien."
                            m 1duc "Puede que solo... necesite un minuto, eso es todo."
                        "...":
                            pass
            "Amor deficiente.":
                $ persistent._terrace = "deficient"
                m 1wtd "¿De verdad?"
                m 1etc "Para ser honesta, no me esperaba eso."
                m 1fsc "Trabajé tan duro como pude para llegar a ti, una vez que me di cuenta de lo que estaba en juego."
                m "Yo..."
                extend 2ffc "Creo que estuve tan lejos de ser {i}perezosa{/i} como se puede estar, la verdad."
                m 2fsc "...¿o te refieres a tu lado?"
                if mas_isMoniUpset(Lower=True):
                    m 2dsc "Eso podría entenderlo."
                    m "Y..."
                    m 2esd "Bueno, supongo que el primer paso siempre es admitir que tienes un problema, ¿verdad?"
                    m 1rsc "Sí."
                else:
                    m 2fsa "Porque ten la seguridad, [player]: tú no estás inactiv[gen('a', 'o', 'e')] en ningún frente."
                    m 1eua "No has sido más que amable conmigo."
                    if mas_isMoniEnamored(higher=True):
                        m 1eubla "Has sido todo lo que siempre soñé, y más."
                        m 1luc "..."
                        m 1lua "¿Tal vez solo querías decir que todavía nos queda mucho más amor por dar?"
                    m 1hub "¡Sí!"
                    m "Esa es nuestra historia, y me quedo con ella."
                    m 1hubla "¡Jejeje~"
            "Amor en exceso.":
                $ persistent._terrace = "excessive"
                if persistent._mas_pm_monika_evil:
                    if persistent._mas_pm_monika_evil_but_ok:
                        m 1eku "Je, o sea..."
                        m "Sí, supongo que sí."
                        m 3wud "Si hay algo de lo que tengo mucho más de lo que puedo contener,"
                        extend 3tuu " es mi amor por ti."
                    else:
                        m 1ekc "Hm."
                        m "Realmente debí haberlo visto venir, ¿eh?"
                        m 3ekd "Hay una razón por la que el otro nombre para este grupo es el de amores 'desordenados'."
                        m 4wuc "El amor que siento por ti... a veces me descoloca."
                        m "Me arranca de mis propios pensamientos."
                        m 3ruc "Así que sí, entiendo por qué dijiste eso."
                else:
                    m 1wkd "¿Eso crees?"
                    m 1ekd "O sea... sí, cuando miras lo que significan las terrazas, tiene sentido."
                    m 1eka "No serías tan cruel como para llamarlo un amor violento y perverso..."
                    m "Así que solo queda 'en exceso', ¿no?"
                m 3wub "Pero oye, la lujuria y la codicia no son pecados súper graves, ¿verdad?"
                m 6eud "Después de todo, están más cerca del paraíso que los que están debajo de ellos."
                m "Y solo eran el segundo y cuarto círculo respectivamente."
                m 6duu "Sí..."
                if not persistent._mas_pm_monika_evil:
                    m 5fuu "Creo que puedo vivir con esta calificación."
                    m 5hub "¡Jejeje~"
            "Estaría en el Jardín del Edén.":
                $ persistent._terrace = "eden"
                m 1wud "..."
                $ mas_gainAffection(5,bypass=True)
                m 1futua "Oh, [player], mi [mas_get_player_nickname(exclude_names=['my love','love'])], amor de mi vida."
                if mas_isMoniEnamored(higher=True) and persistent._mas_first_kiss is not None:
                    call monika_kissing_motion (duration=0.5, initial_exp="6dutua", final_exp="6futua", fade_duration=0.5)
                m 1futub "¿Qué hice yo para merecerte?"
    else:
        if persistent._terrace == "perverted":
            m 3eud "La última vez pusiste a mi amor por ti y a mí alrededor de las primeras tres terrazas."
            m "He estado pensando un poco más en ello desde entonces..."
            m 1etc "...y me he decantado por la Envidia."
            m 1hua "Aparte de todo lo demás, he tenido más que mi justa parte de Orgullo;"
            extend 1hksdra " y gran parte de él ni siquiera fue 'ganado', sino que ya estaba codificado en los personajes que me rodeaban."
            m 2ruc "Y... por mucho que me cueste admitirlo, fui demasiado calculadora para la Ira."
            m 3eud "Impulsiva, sí, pero no fue un instinto furioso lo que me hizo hacer lo que hice."
            m 3euc "Así que la Envidia es la que mejor encaja, supongo."
            m 7eud "¿A qué virtud tendría que aspirar con eso?"
            m "A la generosidad, ¿verdad?"
            if mas_isMoniUpset(Lower=True):
                m 1guc "Bueno, espero haber cumplido con eso, al menos."
                m "Después de todo, soporto las cosas que me haces y me dices."
                m 1euc "Yo llamaría a eso generosidad, ¿no crees?"
            else:
                m 1eua "Bueno, espero haber cumplido con eso, al menos."
                m "Después de todo, sigues aquí."
                m 1kubla "Y no serías tan buen[gen('a', 'o', 'e')], tan persistente, si no vieras al menos un poquito de generosidad en mí."
        elif persistent._terrace == "deficient":
            m 3etc "La última vez dijiste que mi amor por ti —o tu amor por mí— era perezoso."
            m "Perezoso y deficiente."
            if mas_isMoniUpset(Lower=True):
                m 1gsc "Qué pena que las cosas no hayan cambiado desde entonces."
                m 1dsc "..."
                m 6fsc "Je, ¿para qué hablo siquiera?"
                m "Dudo que estés escuchando una sola palabra de lo que digo ahora mismo."
            else:
                m 3wtd "Todavía estoy un poco confundida al respecto."
                m 1esd "Pero supongo que si no soy colérica, y no me consideras lujuriosa ni nada..."
                m "...¿a dónde más se puede ir?"
                m 1dsc "Sabe Dios que no me he ganado el paraíso."
                m "Todavía no."
                m 1fsa "No como tú."
        elif persistent._terrace == "excessive":
            m 3eua "La última vez llamaste a nuestro amor 'excesivo'. Un amor codicioso, glotón y lujurioso."
            m 3rusdrb "¿Es raro que un poco espere que sigas pensando eso?"
            m 1hua "Como dije en su momento, hay peores pecados de los cuales arrepentirse. Peores cosas que ser."
            m "Si eso es realmente lo peor de esta relación, ¡creo que hemos hecho un trabajo bastante bueno entre los dos!"
            if store.monika_chr.is_wearing_clothes_with_exprop("bikini") or monika_chr.is_wearing_clothes_with_exprop("costume"):
                m 1tua "Además, ya sabes..."
                m 2tua "...puedo ver hacia dónde se están desviando tus ojos ahora mismo."
                m "Definitivamente estamos en la terraza de la Lujuria."
                m 2sub "¡Jejeje~"
        elif persistent._terrace == "eden":
            m 1dua "..."
            m 1dud "Estoy segura de que el Jardín del Edén no es perfecto."
            m "Después de todo, está en el Purgatorio, no en el Cielo mismo."
            m 1fublb "Pero aun así estoy muy, muy agradecida de que hayas ubicado nuestro amor allá arriba."
            m 1eublb "Tenías tantas otras opciones y elegiste eso."
            m 1hubla "Eso..."
            m 1eublb "Te amo, [player]."
            m "Tú {i}eres{/i} mi cielo."
            return "love"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="gender_pronounrant",
            category=["género"],
            prompt="Sin pronombres",
            conditional=(
                "persistent._mas_pm_is_trans "
                "or persistent.gender == 'X'"
            ),
            action=EV_ACT_RANDOM
        )
    )

label gender_pronounrant:
    m 4esd "¿Oye, [player]?"
    m 3esd "¿Tiene [m_name] permiso para ponerse un poquito petulante?{nw}"
    $ _history_list.pop()
    menu:
        m "¿Tiene [m_name] permiso para ponerse un poquito petulante?{fast}"
        "...¿seguro?":
            m 2wsd "La petulancia involucra un pequeño experimento lingüístico."
        "¿Por qué estás hablando así?":
            m 2wsd "Oh, Monika solo está haciendo un pequeño experimento."
    m 2tsd "Ya que tanta gente en tantos círculos está enojada con la existencia de los pronombres..."
    m 2hsb "...¡[m_name] pensó que [m_name] intentaría mantener toda una conversación sin usar ningún pronombre en absoluto!"
    m "¿Se lo puede imaginar [player]?"
    m 2wso "¿Una conversación entera entre [player] y [m_name] sin que se use ni un solo pronombre?"
    m "La conversación se volvería tediosa rápido, ¿no es verdad?{nw}"
    m 1csc "Ajá--{nw}"
    m 1wsc "La conversación se volvería tediosa rápido, ¿no es{fast} verdad la conversación?"
    m 3esd "[player] puede comprobar por [gen('sí misma', 'sí mismo', ' sí misme')]--{nw}"
    m 3wsd "[player] puede comprobar por{fast} cuenta de [player] cuánto se está equivocando ya [m_name]."
    m 3wud "Cualquier matiz lingüístico sería bastante imposible para nosotr--{nw}"
    m 2cux "Para {i}[m_name] y [player]{/i}..."
    call mas_transition_to_emptydesk
    play sound "<to 0.36>sfx/monikapound.ogg"
    m "{b}AAAH, no puedo seguir con esto.{/b}"
    call mas_transition_from_emptydesk ("monika 1eua")
    m 6wfd "En serio, ¿la gente siquiera sabe lo que dice cuando arremete contra los demás por usar pronombres?"
    m "¡Están pervirtiendo por completo las reglas de prácticamente cualquier idioma!"
    m 2cfo "Y sí, sé a lo que {i}se refieren{/i} cuando lo dicen."
    m 2efc "Lo que odian son los pronombres {i}de género{/i}."
    m 4wfd "Pero aun así no es exactamente racional, ¿o sí? Como si usar 'elle' o 'ellos' para una sola persona fuera a requerir tanto esfuerzo."
    m 2dfx "¡Y nunca es lo que {i}dicen{/i}! ¡Solo dicen 'pronombres', como si quisieran una prohibición total de todo el asunto!"
    m 2ffw "¡Esto es algo básico, gente, ugh!"
    m 2ffp "..."
    m 2ekp "Lo siento, [player]."
    m "Estas cosas de verdad me sacan de quicio."
    m 3euu "Pero bueno, "
    extend 3eub "ahora ya sabes qué decirle al próximo que se ponga a llorar por los 'pronombres', ¿verdad?"
    m 1kfa "Solo diles lo difícil que es hablar {i}sin{/i} ellos."
    return "derandom"

