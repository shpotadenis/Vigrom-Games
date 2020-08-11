


export default {
    name: 'SearchComponent',
    data(){
      return{
        best:[
              {
              id:"1",
              image:"MaskGroup.svg",
              name:"300$",
              rating:"4.9",
              undername:"Ubisoft Nadeo | Ubisoft",
              price:"299.99",
              scrin:'vessel-5.jpg',
              scrin1:'c97a9.jpg',
              scrin2:'Pic1.jpg',
              scrin3:'c97a9.jpg',
              icon:'cart-icon.png'
              },
              {
              id:"2",
              image:"MaskGroup.svg",
              name:"Yes,sir",
              rating:"4.9",
              undername:"Ubisoft Nadeo | Ubisoft",
              price:"299.99",

              scrin:'vessel-5.jpg',
              scrin1:'c97a9.jpg',
              scrin2:'Pic1.jpg',
              scrin3:'c97a9.jpg',
              icon:'cart-icon.png'
              },
            ],
          bestscomponents:[
                {
                id:"1",
                image:"MaskGroup.svg",
                name:"300$",
                rating:"4.9",
                undername:"Ubisoft Nadeo | Ubisoft",
                price:"299.99",
                scrin:'vessel-5.jpg',
                scrin1:'c97a9.jpg',
                scrin2:'Pic1.jpg',
                scrin3:'c97a9.jpg',
                icon:'cart-icon.png'
                },
                {
                id:"2",
                image:"MaskGroup.svg",
                name:"Yes,sir",
                rating:"4.9",
                undername:"Ubisoft Nadeo | Ubisoft",
                price:"299.99",

                scrin:'vessel-5.jpg',
                scrin1:'c97a9.jpg',
                scrin2:'Pic1.jpg',
                scrin3:'c97a9.jpg',
                icon:'cart-icon.png'
                },
                {
                id:"3",
                image:"MaskGroup.svg",
                name:"WeWE",
                rating:"4.9",
                undername:"Ubisoft Nadeo | Ubisoft",
                price:"299.99",

                scrin:'vessel-5.jpg',
                scrin1:'c97a9.jpg',
                scrin2:'Pic1.jpg',
                scrin3:'c97a9.jpg',
                icon:'cart-icon.png'
                },
                {
                id:"4",
                image:"MaskGroup.svg",
                name:"WeWEwewe",
                rating:"4.9",
                undername:"Ubisoft Nadeo | Ubisoft",
                price:"299.99",

                scrin:'vessel-5.jpg',
                scrin1:'c97a9.jpg',
                scrin2:'Pic1.jpg',
                scrin3:'c97a9.jpg',
                icon:'cart-icon.png'
                },
                {
                id:"5",
                image:"MaskGroup.svg",
                name:"Wecckend",
                rating:"4.9",
                undername:"Ubisoft Nadeo | Ubisoft",
                price:"299.99",

                scrin:'vessel-5.jpg',
                scrin1:'c97a9.jpg',
                scrin2:'Pic1.jpg',
                scrin3:'c97a9.jpg',
                icon:'cart-icon.png'
                },
                {
                id:"6",
                image:"MaskGroup.svg",
                name:"Dangeon Master",
                rating:"4.9",
                undername:"Ubisoft Nadeo | Ubisoft",
                price:"299.99",

                scrin:'vessel-5.jpg',
                scrin1:'c97a9.jpg',
                scrin2:'Pic1.jpg',
                scrin3:'c97a9.jpg',
                icon:'cart-icon.png'
                },
              ],
              isShow:false,
              searchGames:''
      }
    },
    props:['searchzone'],
    methods:{
      showGames(){
        for(let i = 0; i<this.searchData.length; i++){
          if(this.searchData[i].name.toLowerCase().includes(this.searchGames)){
            this.isShow = true
          }
          if(this.searchGames == ''){
            this.isShow = false
          }
        }
      }
    },
    computed:{
      searchData(){
        if(this.searchzone == 'games'){
          return this.bestscomponents.filter(elem => {
          return elem.name.toLowerCase().includes(this.searchGames);
        })
        }else{
          return this.best.filter(elem => {
          return elem.name.toLowerCase().includes(this.searchGames);
        }
      );

    }

}
}
}
