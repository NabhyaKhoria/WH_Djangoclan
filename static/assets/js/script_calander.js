const date = new Date();

const renderCalendar = () => {
  date.setDate(1);

  const monthDays = document.querySelector(".days");

  const lastDay = new Date(
    date.getFullYear(),
    date.getMonth() + 1,
    0
  ).getDate();

  const prevLastDay = new Date(
    date.getFullYear(),
    date.getMonth(),
    0
  ).getDate();

  const firstDayIndex = date.getDay();

  const lastDayIndex = new Date(
    date.getFullYear(),
    date.getMonth() + 1,
    0
  ).getDay();

  const nextDays = 7 - lastDayIndex - 1;

  const months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];

  document.querySelector(".date h1").innerHTML = months[date.getMonth()];

  document.querySelector(".date p").innerHTML = new Date().toDateString();

  let days = "";

  for (let x = firstDayIndex; x > 0; x--) {
    days += `<div class="prev-date">${prevLastDay - x + 1}</div>`;
  }

  const formatDate = (date) => {
    if (date.toString().length === 1) {
      return `0${date}`;
    } else {
      return date;
    }
  };

  for (let i = 1; i <= lastDay; i++) {
    if (
      i === new Date().getDate() &&
      date.getMonth() === new Date().getMonth()
    ) {
      
      days += `<div class="${formatDate(i)}-${formatDate(date.getMonth()+1)}-${date.getFullYear()} datum today ">${i}</div>`;
    } else {
      days += `<div class="${formatDate(i)}-${formatDate(date.getMonth()+1)}-${date.getFullYear()} datum">${i}</div>`;
    }
  }

  for (let j = 1; j <= nextDays; j++) { 
    days += `<div class="next-date">${j}</div>`;
    monthDays.innerHTML = days;
  }
};

document.querySelector(".prev").addEventListener("click", () => {
  date.setMonth(date.getMonth() - 1);
  renderCalendar();
  refresh();
});

document.querySelector(".next").addEventListener("click", () => {
  date.setMonth(date.getMonth() + 1);
  renderCalendar();
  refresh();
});


renderCalendar();
refresh();




  function refresh(){
    console.log("Refreshing");
    var dates = document.querySelectorAll(".datum");
    var d = Array.from(document.getElementById("data-calendar").children);
  // console.log(d);
  // console.log(dates[0].classList[0]);
  // console.log(d.options[0].value);
    dates.forEach(date => {
      
      
      console.log(date.classList[0]);
      
    })
//("0" + (this.getMonth() + 1)).slice(-2)
    d.forEach(date => {
      console.log(date.options[0].value);
      
    })

  dates.forEach(date => {
    const i = d.findIndex(d => d.options[0].value==date.classList[0]);
    // console.log(i);
    if(i !== -1){
      const eventCard = document.createElement("div");
      eventCard.classList.add("eventCard");
      eventCard.innerHTML = `
        
        <p style="color: white">${d[i].options[1].value}</p>
      `;
      date.appendChild(eventCard);

      date.addEventListener('mouseover', () => {
        eventCard.classList.add("eventCard__showEvent");
        document.querySelector("#entry1").innerText = d[i].options[1].value;
      })
      date.addEventListener('mouseout', () => {
        eventCard.classList.remove("eventCard__showEvent");
        document.querySelector("#entry1").innerHTML = "";
      })
    }
  })
  }
  
  // dates.forEach(el => {
  //   el.addEventListener('mouseover', () => {
  //     if(el.classList.contains(page.children[j].options[0].value)) {
  //       document.querySelector(".notif").style.display = "block";
  //       alert("adv")
  //     }
      
  
  //   })
  //   el.addEventListener('mouseout', () => {
  //     document.querySelector(".notif").style.display = "none";
  //   })
  // })
