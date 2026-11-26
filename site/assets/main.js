(function(){
  // Menu mobile
  var burger=document.querySelector('.burger'),drawer=document.getElementById('drawer');
  if(burger&&drawer){
    var setMenu=function(open){drawer.classList.toggle('open',open);burger.setAttribute('aria-expanded',open);burger.setAttribute('aria-label',open?'Fermer le menu':'Ouvrir le menu');burger.querySelector('use').setAttribute('href',open?'#i-x':'#i-menu');};
    burger.addEventListener('click',function(){setMenu(!drawer.classList.contains('open'))});
    drawer.addEventListener('click',function(e){if(e.target.closest('a'))setMenu(false)});
    document.addEventListener('keydown',function(e){if(e.key==='Escape')setMenu(false)});
  }
  // Menu déroulant Solutions
  document.querySelectorAll('.dd').forEach(function(dd){
    var b=dd.querySelector('button');
    b.addEventListener('click',function(e){e.stopPropagation();var o=!dd.classList.contains('open');dd.classList.toggle('open',o);b.setAttribute('aria-expanded',o);});
    document.addEventListener('click',function(){dd.classList.remove('open');b.setAttribute('aria-expanded','false')});
  });
  // Formulaire de contact (FormSubmit)
  var form=document.getElementById('form-devis');
  if(form){
    var params=new URLSearchParams(location.search),besoin=params.get('besoin');
    if(besoin){var s=document.getElementById('besoin');for(var i=0;i<s.options.length;i++){if(s.options[i].text===besoin)s.selectedIndex=i;}}
    var status=document.getElementById('form-status');
    form.addEventListener('submit',function(e){
      e.preventDefault();
      var btn=form.querySelector('button[type=submit]');btn.disabled=true;btn.style.opacity=.7;status.textContent='Envoi en cours…';status.style.color='';
      fetch(form.action.replace('formsubmit.co/','formsubmit.co/ajax/'),{method:'POST',body:new FormData(form),headers:{Accept:'application/json'}})
        .then(function(r){return r.json()})
        .then(function(d){if(d.success===true||d.success==='true'){location.href='merci.html';}else{throw new Error()}})
        .catch(function(){btn.disabled=false;btn.style.opacity='';status.style.color='#c2410c';status.innerHTML='Envoi impossible pour le moment. Appelez-nous au <a href="tel:+33695607875">06 95 60 78 75</a>.';});
    });
  }
  var y=document.getElementById('y');if(y)y.textContent=new Date().getFullYear();
})();
