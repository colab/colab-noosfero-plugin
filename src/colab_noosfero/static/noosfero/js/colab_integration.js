/*
    The below variables was declared in
    colab/colab/plugins/noosfero/templates/proxy/noosfero.html:

    community         - community name from the noosfero
    repository        - url for the community's repository
    mailman_list      - list name linked with the community
    threads_limit     - Number of threadsthat will be displayed
    activities_limit  - Number of activities that will be displayed
*/

$(transform_tags);

function  transform_tags()
{
       discussion_tag();
       feed_gitlab_tag();
}

function feed_gitlab_tag()
{
       var $tag = $('#repository-feed-tab');
       $tag.text("Esta comunidade não está associada a"+
                 " nenhum repositório no momento, para mais"+
                 " detalhes contate o administrador");

       $.getJSON(repository, {limit:activities_limit, offset:0},function(msg, e){
             $tag.html(msg.html);
             $tag.append("<div class=\"see-more-repository\">"+
					   "<a href="+repository+">"+
					   "veja toda a atividade no repositório"+
					   "</a></div>");
       });
}

function discussion_tag()
{
       var $tag = $('#discussions-tab');
       var request_path = '/spb/get_list/'+
                          '?list_name='+mailman_list+
                          '&MAX='+list_limit;
       $tag.load(request_path);
}
