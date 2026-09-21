async function loadStatus(){
  const r=await fetch("data/status.json",{cache:"no-store"});
  if(!r.ok) throw new Error("상태 데이터를 불러오지 못했습니다.");
  return r.json();
}

function el(tag,cls,text){
  const n=document.createElement(tag);
  if(cls)n.className=cls;
  if(text!==undefined)n.textContent=text;
  return n;
}

const statusLabel={
  "in-progress":"진행 중",
  "blocked":"대기/막힘",
  "queued":"예정"
};

loadStatus().then(data=>{
  document.querySelector("#current-stage").textContent=data.currentStage;
  document.querySelector("#goal").textContent=data.goal;
  document.querySelector("#blocker").textContent=data.currentBlocker;
  document.querySelector("#updated").textContent="마지막 동기화: "+data.updated;

  const phases=document.querySelector("#phases");
  data.phases.forEach(p=>{
    const card=el("article","phase");
    const badge=el("span","status "+p.status,statusLabel[p.status]||p.status);
    card.appendChild(badge);
    card.appendChild(el("h3","","단계 "+p.id+" — "+p.title));

    const bar=el("div","bar");
    const fill=el("span");
    fill.style.width=(p.progress||0)+"%";
    bar.appendChild(fill);
    card.appendChild(bar);
    card.appendChild(el("div","",(p.progress||0)+"%"));

    const a=el("a","","GitHub 이슈 #"+p.issue+" →");
    a.href="https://github.com/TaekGyu0801/GGYU/issues/"+p.issue;
    card.appendChild(a);
    phases.appendChild(card);
  });

  const members=document.querySelector("#members");
  data.members.forEach(m=>{
    const card=el("article","member");
    card.appendChild(el("div","eyebrow","연구원"));
    card.appendChild(el("h3","",m.name));
    card.appendChild(el("p","",m.role));

    const a=el("a","","작업 공간 →");
    a.href="https://github.com/TaekGyu0801/GGYU/tree/main/"+m.folder;
    card.appendChild(a);
    members.appendChild(card);
  });

  [["#confirmed","confirmed"],["#unresolved","unresolved"]].forEach(pair=>{
    const ul=document.querySelector(pair[0]);
    data[pair[1]].forEach(x=>ul.appendChild(el("li","",x)));
  });
}).catch(err=>{
  document.querySelector("#current-stage").textContent="대시보드 데이터를 불러오지 못했습니다.";
  document.querySelector("#blocker").textContent=err.message;
});