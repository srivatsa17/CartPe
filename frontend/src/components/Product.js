import React from "react";
import { Card } from "react-bootstrap";
import Rating from "./Rating";
import { Link } from "react-router-dom";

function Product({ product }) {
    return (
        <Card className="my-3 p-3 rounded">
            <Link
                to={`/product/${product._id}`}
                data-testid="product-link-by-image"
            >
                <Card.Img src={product.image} alt="product-image"></Card.Img>
            </Link>
            <Card.Body>
                <Link
                    to={`/product/${product._id}`}
                    style={{ color: "black", textDecoration: "none" }}
                    data-testid="product-link-by-name"
                >
                    <Card.Title as="div">
                        <strong>{product.name}</strong>
                    </Card.Title>
                </Link>

                <Card.Text as="div">
                    <div className="my-3">
                        <Rating rating={product.rating} text={`${product.numReviews} reviews`} />
                    </div>
                </Card.Text>

                <Card.Text as='div'>
                    <h3>
                        Rs. {product.price}
                    </h3>
                </Card.Text>
            </Card.Body>
        </Card>
    );
}

export default Product;