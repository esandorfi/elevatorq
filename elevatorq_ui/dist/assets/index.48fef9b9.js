import{p as e,a,r as t,o as s,c as l,b as o,t as n,u as d,F as i,d as r,e as c,f as u}from"./vendor.82d93468.js";e("data-v-d415dcd8");const p=o("p",null,[o("a",{href:"https://vitejs.dev/guide/features.html",target:"_blank"}," Vite Documentation "),r(" | "),o("a",{href:"https://v3.vuejs.org/",target:"_blank"},"Vue 3 Documentation")],-1),m=o("p",null,[r(" Edit "),o("code",null,"components/HelloWorld.vue"),r(" to test hot module replacement. ")],-1);a();const b={expose:[],props:{msg:String},setup(e){const a=t({count:0});return(t,r)=>(s(),l(i,null,[o("h1",null,n(e.msg),1),p,o("button",{onClick:r[1]||(r[1]=e=>d(a).count++)},"count is: "+n(d(a).count),1),m],64))},__scopeId:"data-v-d415dcd8"},f={},v={class:"navbar navbar-light bg-light"},h=c('<div class="container-fluid"><a class="navbar-brand" href="/"> Elevator Q </a><div class="d-flex"><div class="form-check form-switch me-5 d-flex align-items-center"><input class="form-check-input" type="checkbox" id="flexSwitchCheckDefault" disabled><label class="form-check-label" for="flexSwitchCheckDefault"> system on/off</label></div><a href="/admin" class="btn btn-dark me-2">admin</a><div class="dropdown me-2"><button class="btn btn-outline-dark dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false"> api </button><ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1"><li><a class="dropdown-item" href="/api/building/">api building</a></li><li><a class="dropdown-item" href="/api/elevatorq/">api elevatorq</a></li><li><a class="dropdown-item" href="/api/pressbtnq/">api pressbtnq</a></li></ul></div><a href="https://gitlab.com/esandorfi/elevatorq/-/tree/master/docs/iter3" class="btn btn-outline-dark me-5">readme</a></div></div>',1);f.render=function(e,a){return s(),l("nav",v,[h])};const g=o("div",{class:"hero"},[o("img",{alt:"logo",src:"/assets/elevator-svgrepo-com.2f610d9f.svg",width:"300"}),o("h1",null,"Elevator Q")],-1);u({expose:[],setup:e=>(e,a)=>(s(),l("div",null,[o(f),g,o(b,{msg:"Hello Vue 3 + Vite"})]))}).mount("#app");