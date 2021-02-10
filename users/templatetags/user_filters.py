from django import template

register = template.Library()

@register.filter 
def addclass(field, css):
        return field.as_widget(attrs={"class": css})
        
@register.simple_tag(takes_context=True)
def distinct(context, items):
    
    user = context['user']
    items = [item for item in items if item.user == user]
    return items


@register.filter
def dist(items):
    if len(items)>= 3:
        items = [items[i] for i in range(0,3)]
        len_items = len(items)
    return items

@register.simple_tag
def dist_tag(items):
    
    len_items = len(items)-3
    return len_items

@register.filter
def tags_add(request, tag):
    
    list_tag =[v for k,v in request.GET.lists()]
    if list_tag:
        if len(list_tag[0])==1:
            request = "tag=" +str(list_tag[0][0]) + "&tag=" +str(tag)
            return request 
        else:
            request = "tag=" +str(list_tag[0][0]) + "&tag=" +str(list_tag[0][1]) + "&tag=" +str(tag)
            return request

    request = "tag=" +str(tag)
    return request


@register.filter
def tags_delete(request, tag):
    
    list_tag =[v for k,v in request.GET.lists()]
    if list_tag:
        list_tag[0].remove(tag)
        if len(list_tag[0])==2:
            request = "tag=" +str(list_tag[0][0]) + "&tag=" +str(list_tag[0][1])
            return request 
        elif len(list_tag[0])==1:
            request = "tag=" +str(list_tag[0][0]) 
            return request

   
    
    
    
    
    