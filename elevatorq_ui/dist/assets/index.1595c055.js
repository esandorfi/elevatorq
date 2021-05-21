import{p as e,a as t,r as a,o as s,c as n,b as o,t as l,u as d,F as r,d as i,e as c,f as u}from"./vendor.82d93468.js";e("data-v-d415dcd8");const p=o("p",null,[o("a",{href:"https://vitejs.dev/guide/features.html",target:"_blank"}," Vite Documentation "),i(" | "),o("a",{href:"https://v3.vuejs.org/",target:"_blank"},"Vue 3 Documentation")],-1),f=o("p",null,[i(" Edit "),o("code",null,"components/HelloWorld.vue"),i(" to test hot module replacement. ")],-1);t();const m={expose:[],props:{msg:String},setup(e){const t=a({count:0});return(a,i)=>(s(),n(r,null,[o("h1",null,l(e.msg),1),p,o("button",{onClick:i[1]||(i[1]=e=>d(t).count++)},"count is: "+l(d(t).count),1),f],64))},__scopeId:"data-v-d415dcd8"},b={},v={class:"navbar navbar-light bg-light"},h=c('<div class="container-fluid"><a class="navbar-brand" href="/"> Elevator Q </a><div class="d-flex"><a href="/admin" class="btn btn-dark me-2">admin</a><div class="dropdown me-2"><button class="btn btn-outline-dark dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false"> api </button><ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1"><li><a class="dropdown-item" href="/api/building/">api building</a></li><li><a class="dropdown-item" href="/api/elevatorq/">api elevatorq</a></li><li><a class="dropdown-item" href="/api/pressbtnq/">api pressbtnq</a></li></ul></div><a href="https://gitlab.com/esandorfi/elevatorq/-/tree/master/docs/iter3" class="btn btn-outline-dark me-5">readme</a></div></div>',1);b.render=function(e,t){return s(),n("nav",v,[h])};const g={},w={class:"d-flex justify-content-end p-3"},k=o("div",{class:"form-check form-switch me-5 d-flex align-items-center"},[o("input",{class:"form-check-input",type:"checkbox",id:"flexSwitchCheckDefault",disabled:""}),o("label",{class:"form-check-label",for:"flexSwitchCheckDefault"}," system on/off")],-1);g.render=function(e,t){return s(),n("div",w,[k])};const x=o("div",{class:"hero"},[o("img",{alt:"logo",src:"/assets/elevator-svgrepo-com.2f610d9f.svg",width:"300"}),o("h1",null,"Elevator Q")],-1);u({expose:[],setup:e=>(e,t)=>(s(),n("div",null,[o(b),o(g),x,o(m,{msg:"Hello Vue 3 + Vite"})]))}).mount("#app");