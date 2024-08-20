from serviceapresvente.models import Sav_request
from serviceapresvente.models import CommandeSav
from serviceapresvente.models import SuiviCommandeSav
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from serviceapresvente.forms.CommandeSavForm import CommandeSavForm
from django.db import IntegrityError

def index(request):
    #commandesavs_list = CommandeSav.objects.prefetch_related('savrequest').all()
    commandesavs_list = CommandeSav.objects.all()   #prefetch_related('savrequest').all()
    paginator = Paginator(commandesavs_list, 8)
    page = request.GET.get('page', 1)
    formCommandeUpd = CommandeSavForm()

    try:
        commandesavs = paginator.page(page)
    except PageNotAnInteger:
        commandesavs = paginator.page(1)
    except EmptyPage:
        commandesavs = paginator.page(paginator.num_pages)
    except:
        commandesavs = paginator.page(1)

    return render(request,"servicedsi/index.html",{
    'page':'savrequest',
    'subpage':'commandesav',
    'commandesavs_list':commandesavs_list,
    'formCommandeUpd':formCommandeUpd
    })
# Les autres fonctions comme show, create, update, delete... 

def show(request, id):
    commandesav = get_object_or_404(CommandeSav, idcommandesav=id)
    detailformUpd = CommandeSavForm(instance=commandesav)
    return render(request, 'servicedsi/commandesav/formcommandeDetail.html/', 
                  {'commandesav': commandesav,
                   'detailformUpd':detailformUpd
                   })

"""
def create(request):
    if request.method == 'POST':
        form = CommandeSavForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False) 
            if(data.statut == "commande placée" ):
                try:
                    suicommandesav, created = SuiviCommandeSav.objects.get_or_create(
                            commandesav_id = data.idcommandesav,
                            )
                    if created:
                        ### Mise a jour de status dans SAV Request
                        Sav_request_instance = Sav_request.objects.get(pk=data.savrequest.idrequest)
                        Sav_request_instance.status = 'pending (logistique)'
                        Sav_request_instance.save()
                        data.flag = True
                        data.save()
                        messages.success(request, 'Processus Logistique!')
                except IntegrityError:
                        messages.error(request, 'Erreur d\'intégrité lors de la création du processus achat !')
            else: 
                data.save()
                messages.success(request, 'CommandeSav has been saved !')
        return redirect('serviceapresvente:commandesav-index')
        
    else:
        form = CommandeSavForm()
    return render(request, 'servicedsi/', {'form': form})
"""

def update(request, id):
    commandesav = get_object_or_404(CommandeSav, idcommandesav=id)
    print('request.method:',request.method)
    if request.method == 'POST':
        if request.POST.get('_method') == 'PUT':
            form = CommandeSavForm(request.POST, request.FILES, instance=commandesav)
            if form.is_valid():
                data = form.save(commit=False) 
                if(data.statut == "commande placée" ):
                    try:
                        suicommandesav, created = SuiviCommandeSav.objects.get_or_create(
                                commandesav_id = data.idcommandesav,
                                )
                        if created:
                            ### Mise a jour de status dans SAV Request
                            Sav_request_instance = Sav_request.objects.get(pk=data.savrequest.idrequest)
                            Sav_request_instance.statut = 'pending (logistique)'
                            Sav_request_instance.save()
                            data.flag = True
                            data.save()
                            #print('success')
                            messages.success(request, 'Processus Logistique!')
                            
                        else:
                            messages.warning(request, 'Le suivi de commande existe déjà.')    
                    except IntegrityError:
                            messages.error(request, 'Erreur d\'intégrité lors de la création du processus achat !')
                else: 
                    data.save()
                    print('success')
                    messages.success(request, 'CommandeSav has been saved !')
                return redirect('serviceapresvente:commandesav')
            else:
                print('form invalid:')
                messages.error(request, 'Le formulaire est invalide. Veuillez vérifier les champs.')
                form = CommandeSavForm(instance=commandesav)
        else:
            form = CommandeSavForm(instance=commandesav)
            print('La méthode PUT n\'a pas été trouvée.')
    else:
        form = CommandeSavForm(instance=commandesav)
        print('No POST method:')
    return render(request, 'servicedsi/commandesav/formCommandeUpd.html', 
                   {'form': form, })

def delete(request, id):
    commandesav = get_object_or_404(CommandeSav, idcommandesav=id)
    if request.method == 'POST':
        if request.POST.get('_method') == 'DELETE':
            commandesav.delete()
            messages.success(request, 'CommandeSav has been deleted !')
    return redirect('serviceapresvente:commandesav')

