import '../../../css/ProductSearchScreen/SortBy/SortBy.css';

import React, { useEffect, useRef, useState } from "react";

import { Col } from 'react-bootstrap';
import SortByInput from "./SortByInput";
import SortByMenu from "./SortByMenu";
import { useSearchParams } from 'react-router-dom';

const sortByOptions = [
    { value : "name", label : "Recommended"},
    { value : "new", label : "What's New"},
    { value : "popularity", label : "Popularity"},
    { value : "discount", label : "Better discount"},
    { value : "price_desc", label : "Price: High to Low"},
    { value : "price_asc", label : "Price: Low to High"},
    { value : "rating", label : "Customer Rating"}
];

function SortBy() {
    const sortByRef = useRef(null);
    const [showSortByMenu, setShowSortByMenu] = useState(false);
    const [selectedSortByValue, setSelectedSortByValue] = useState(null);
    const [queryParams, setQueryParams] = useSearchParams();

    useEffect(() => {
        const handleClickOutside = (event) => {
            if(sortByRef.current && !sortByRef.current.contains(event.target)) {
                setShowSortByMenu(false);
            }
        };
        document.addEventListener('mousedown', handleClickOutside);
        return () => {
            document.removeEventListener('mousedown', handleClickOutside);
        };
    })

    const handleSortByMenuOnMouseOver = (value) => {
        setShowSortByMenu(value);
    }

    const handleSortByItemClick = (option) => {
        setSelectedSortByValue(option.label);
        queryParams.set('sort', option.value);
        setQueryParams(queryParams, { replace: true });
    }

    return (
        <Col className="sort-by-container" ref={sortByRef}>
            <SortByInput
                handleSortByMenuOnMouseOver={handleSortByMenuOnMouseOver}
                selectedSortByValue={selectedSortByValue}
                sortByOptions={sortByOptions}
            />
            <SortByMenu
                showSortByMenu={showSortByMenu}
                handleSortByItemClick={handleSortByItemClick}
                sortByOptions={sortByOptions}
            />
        </Col>
    );
}

export default SortBy;