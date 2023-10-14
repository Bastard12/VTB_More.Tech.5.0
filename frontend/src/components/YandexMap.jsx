import React, { useEffect, useRef } from "react";

const YandexMap = () => {
    const mapRef = useRef(null);

    useEffect(() => {
        // Загрузка API Яндекс.Карт
        const script = document.createElement("script");
        script.src = "https://api-maps.yandex.ru/2.1/?apikey=5941ca0f-88a5-462a-b68b-049e98bd248c&lang=ru_RU";
        script.async = true;
        document.body.appendChild(script);

        script.onload = () => {
            // Инициализация карты внутри функции ymaps.ready()
            window.ymaps.ready(() => {
                const map = new window.ymaps.Map(mapRef.current, {
                    center: [55.75, 37.57],
                    zoom: 10,
                });

                const placemark = new window.ymaps.Placemark([55.75, 37.57], {}, {});
                map.geoObjects.add(placemark);
            });
        };
    }, []);

    return <div ref={mapRef} style={{ width: "1176px", height: "640px" }} />;
};

export default YandexMap;
