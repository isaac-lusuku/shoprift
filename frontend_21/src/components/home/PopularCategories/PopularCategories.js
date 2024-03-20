import { React } from "react";
import Flex from "../../designLayouts/Flex";
import { CgMenuGridO } from "react-icons/cg";
import { Link } from "react-router-dom";
import Image from "../../designLayouts/Image";


const CategoryDsign = ({imgScr, text}) =>{
   return  (<div className="flex flex-col gap-5">
        <img  className=" w-24" src={imgScr}/>
    </div>)
}

const categories = [
    {
        imgScr: "https://img.freepik.com/fotos-gratis/design-de-interiores-minimalista_23-2150870800.jpg?t=st=1710877596~exp=1710881196~hmac=65441728d75e3526802a53fb1b6301a5a62d5fe0c970de5689a6c48534d3e746&w=2000",
        text: "yoo testing"
    },
    {
        imgScr: "https://img.freepik.com/fotos-gratis/design-de-interiores-minimalista_23-2150870800.jpg?t=st=1710877596~exp=1710881196~hmac=65441728d75e3526802a53fb1b6301a5a62d5fe0c970de5689a6c48534d3e746&w=2000",
        text: ""
    },
    {
        imgScr: "https://img.freepik.com/fotos-gratis/design-de-interiores-minimalista_23-2150870800.jpg?t=st=1710877596~exp=1710881196~hmac=65441728d75e3526802a53fb1b6301a5a62d5fe0c970de5689a6c48534d3e746&w=2000",
        text: ""
    },
    {
        imgScr: "https://img.freepik.com/fotos-gratis/design-de-interiores-minimalista_23-2150870800.jpg?t=st=1710877596~exp=1710881196~hmac=65441728d75e3526802a53fb1b6301a5a62d5fe0c970de5689a6c48534d3e746&w=2000",
        text: ""
    },
    {
        imgScr: "https://img.freepik.com/fotos-gratis/design-de-interiores-minimalista_23-2150870800.jpg?t=st=1710877596~exp=1710881196~hmac=65441728d75e3526802a53fb1b6301a5a62d5fe0c970de5689a6c48534d3e746&w=2000",
        text: ""
    },
    {
        imgScr: "https://img.freepik.com/fotos-gratis/design-de-interiores-minimalista_23-2150870800.jpg?t=st=1710877596~exp=1710881196~hmac=65441728d75e3526802a53fb1b6301a5a62d5fe0c970de5689a6c48534d3e746&w=2000",
        text: ""
    },
    {
        imgScr: "https://img.freepik.com/fotos-gratis/design-de-interiores-minimalista_23-2150870800.jpg?t=st=1710877596~exp=1710881196~hmac=65441728d75e3526802a53fb1b6301a5a62d5fe0c970de5689a6c48534d3e746&w=2000",
        text: ""
    }
]

const PopularCategories = () =>{
    return (<div className="h-screen sm:h-[45vh] flex-col">
        <div className="flex justify-between h-1/6 items-center">
            <div className="flex gap-1 ml-20 text-2xl font-semibold">
                 <CgMenuGridO className="text-3xl text-themeColor" />
                <p >Explore Popular Categories</p>
            </div>
            <Link to="/shop">
                 <p  className="mr-20 text-xl hover:underline">see all</p>
            </Link>
        </div>
        <Flex className="flex gap-6 justify-center items-center bg-black h-5/6 w-11/12 mx-auto">
        {categories.map((category) => (
          <CategoryDsign {...category} />
        ))}
        </Flex>
    </div>)
}
export default PopularCategories