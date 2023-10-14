import React, { useEffect, useRef, useState } from "react";

const YandexMap = () => {
    const [isLoaded, setIsLoaded] = useState(false);
    const mapRef = useRef(null);

    useEffect(() => {
        // Загрузка API Яндекс.Карт
        const script = document.createElement("script");
        script.src =
            "https://api-maps.yandex.ru/2.1/?apikey=5941ca0f-88a5-462a-b68b-049e98bd248c&lang=ru_RU";
        script.async = true;
        document.body.appendChild(script);

        script.onload = () => {
            // Установка значения isLoaded в true при загрузке API
            setIsLoaded(true);
        };
    }, []);

    useEffect(() => {
        // Отрисовка карты только после загрузки API
        if (isLoaded) {
            window.ymaps.ready(() => {
                const map = new window.ymaps.Map(mapRef.current, {
                    center: [55.75, 37.57],
                    zoom: 10,
                });
            });
        }
    }, [isLoaded]);

    return (
        <div ref={mapRef} style={{ width: "1176px", height: "640px" }} />
    );
};

export default YandexMap;