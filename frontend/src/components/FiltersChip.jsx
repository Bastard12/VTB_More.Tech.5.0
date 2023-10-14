import { useState } from "react";

export const FiltersChip = () => {
    const [isActive, setIsActive] = useState(false);

    const handleClick = () => {
        setIsActive(!isActive);
    }

    return (
        <button
            className={`w-[118px] h-[40px] shadow shadow-blue-200 rounded text-blue-900 bg-blue-100 font-VTBFontMedium`}
            onClick={handleClick}
        >
            Обмен валюты
        </button>
    );
};
