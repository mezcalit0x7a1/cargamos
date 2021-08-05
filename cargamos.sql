--
-- PostgreSQL database dump
--

-- Dumped from database version 12.7 (Ubuntu 12.7-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.7 (Ubuntu 12.7-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: branches; Type: TABLE; Schema: public; Owner: luis
--

CREATE TABLE public.branches (
    name character varying(255) NOT NULL,
    id integer NOT NULL
);


ALTER TABLE public.branches OWNER TO luis;

--
-- Name: branches_id_seq; Type: SEQUENCE; Schema: public; Owner: luis
--

CREATE SEQUENCE public.branches_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.branches_id_seq OWNER TO luis;

--
-- Name: branches_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: luis
--

ALTER SEQUENCE public.branches_id_seq OWNED BY public.branches.id;


--
-- Name: categories; Type: TABLE; Schema: public; Owner: luis
--

CREATE TABLE public.categories (
    id integer NOT NULL,
    name character varying(25) NOT NULL
);


ALTER TABLE public.categories OWNER TO luis;

--
-- Name: categories_id_seq; Type: SEQUENCE; Schema: public; Owner: luis
--

CREATE SEQUENCE public.categories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.categories_id_seq OWNER TO luis;

--
-- Name: categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: luis
--

ALTER SEQUENCE public.categories_id_seq OWNED BY public.categories.id;


--
-- Name: products; Type: TABLE; Schema: public; Owner: luis
--

CREATE TABLE public.products (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    id_category integer NOT NULL,
    id_branch integer NOT NULL
);


ALTER TABLE public.products OWNER TO luis;

--
-- Name: products_id_seq; Type: SEQUENCE; Schema: public; Owner: luis
--

CREATE SEQUENCE public.products_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.products_id_seq OWNER TO luis;

--
-- Name: products_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: luis
--

ALTER SEQUENCE public.products_id_seq OWNED BY public.products.id;


--
-- Name: stores; Type: TABLE; Schema: public; Owner: luis
--

CREATE TABLE public.stores (
    zip_code character varying(10) NOT NULL,
    phone character varying(10) NOT NULL,
    name character varying(300) NOT NULL,
    id integer NOT NULL,
    email character varying(200) NOT NULL,
    city character varying(50) NOT NULL,
    address character varying(200) NOT NULL,
    state character varying(50) NOT NULL
);


ALTER TABLE public.stores OWNER TO luis;

--
-- Name: store_id_seq; Type: SEQUENCE; Schema: public; Owner: luis
--

CREATE SEQUENCE public.store_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.store_id_seq OWNER TO luis;

--
-- Name: store_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: luis
--

ALTER SEQUENCE public.store_id_seq OWNED BY public.stores.id;


--
-- Name: store_products; Type: TABLE; Schema: public; Owner: luis
--

CREATE TABLE public.store_products (
    id integer NOT NULL,
    sku character varying(50) NOT NULL,
    stock integer NOT NULL,
    price numeric NOT NULL,
    product_id integer NOT NULL,
    store_id integer NOT NULL
);


ALTER TABLE public.store_products OWNER TO luis;

--
-- Name: store_products_id_seq; Type: SEQUENCE; Schema: public; Owner: luis
--

CREATE SEQUENCE public.store_products_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.store_products_id_seq OWNER TO luis;

--
-- Name: store_products_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: luis
--

ALTER SEQUENCE public.store_products_id_seq OWNED BY public.store_products.id;


--
-- Name: branches id; Type: DEFAULT; Schema: public; Owner: luis
--

ALTER TABLE ONLY public.branches ALTER COLUMN id SET DEFAULT nextval('public.branches_id_seq'::regclass);


--
-- Name: categories id; Type: DEFAULT; Schema: public; Owner: luis
--

ALTER TABLE ONLY public.categories ALTER COLUMN id SET DEFAULT nextval('public.categories_id_seq'::regclass);


--
-- Name: products id; Type: DEFAULT; Schema: public; Owner: luis
--

ALTER TABLE ONLY public.products ALTER COLUMN id SET DEFAULT nextval('public.products_id_seq'::regclass);


--
-- Name: store_products id; Type: DEFAULT; Schema: public; Owner: luis
--

ALTER TABLE ONLY public.store_products ALTER COLUMN id SET DEFAULT nextval('public.store_products_id_seq'::regclass);


--
-- Name: stores id; Type: DEFAULT; Schema: public; Owner: luis
--

ALTER TABLE ONLY public.stores ALTER COLUMN id SET DEFAULT nextval('public.store_id_seq'::regclass);


--
-- Data for Name: branches; Type: TABLE DATA; Schema: public; Owner: luis
--

COPY public.branches (name, id) FROM stdin;
Apple	1
Nike	3
Samsung	2
Steren	5
\.


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: luis
--

COPY public.categories (id, name) FROM stdin;
1	Smartphone
2	TV
3	Tennis
4	Tablet
6	Webcam
7	Laptop
\.


--
-- Data for Name: products; Type: TABLE DATA; Schema: public; Owner: luis
--

COPY public.products (id, name, id_category, id_branch) FROM stdin;
1	Iphone SE Rojo 60GB 2012	1	1
4	Iphone SE Negro 60GB 2012	1	1
6	Webcam USB Full HD COM-122	6	5
5	Macbook PRO MID 2012 Silver 500GB	7	1
\.


--
-- Data for Name: store_products; Type: TABLE DATA; Schema: public; Owner: luis
--

COPY public.store_products (id, sku, stock, price, product_id, store_id) FROM stdin;
4	SPISE2BL60	37	12000.00	4	1
9	WEBUSB9087234	98	666.0	6	1
1	SPISE2RED60	0	12000.00	1	1
\.


--
-- Data for Name: stores; Type: TABLE DATA; Schema: public; Owner: luis
--

COPY public.stores (zip_code, phone, name, id, email, city, address, state) FROM stdin;
1234	9981234567	El señor de la tienda	1	sr.tienda@gmail.com	Puerto Morelos	Se casa #400 col. Santa Fe	Quintana Roo
1234	9986565412	Tienda Esotérica	2	esoterica@gmail.com	Puerto Morelos	Brillo Nocturno #666 Col. Hogwarts	Quintana Roo
1233	9986569999	Nueva Era	3	newage@gmail.com	Puerto Morelos	Calle Pato #12, col. Musicales divinos	Quintana Roo
1999	9980908765	La tienda de los testeos	7	test@gmail.com	Solidaridad	El más allá #333, col. Algo	Quintana Roo
1999	9841256956	Tienda su sagrada actualización	5	updated@gmail.com	Solidaridad	Test #987, col. Ceviche	Quintana Roo
1234	9847658900	Gamer Store	6	gamerstore@gmail.com	Solidaridad	Fornite #123 col. Sin Tiempo	Quintana Roo
\.


--
-- Name: branches_id_seq; Type: SEQUENCE SET; Schema: public; Owner: luis
--

SELECT pg_catalog.setval('public.branches_id_seq', 5, true);


--
-- Name: categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: luis
--

SELECT pg_catalog.setval('public.categories_id_seq', 7, true);


--
-- Name: products_id_seq; Type: SEQUENCE SET; Schema: public; Owner: luis
--

SELECT pg_catalog.setval('public.products_id_seq', 7, true);


--
-- Name: store_id_seq; Type: SEQUENCE SET; Schema: public; Owner: luis
--

SELECT pg_catalog.setval('public.store_id_seq', 7, true);


--
-- Name: store_products_id_seq; Type: SEQUENCE SET; Schema: public; Owner: luis
--

SELECT pg_catalog.setval('public.store_products_id_seq', 9, true);


--
-- Name: branches branches_pkey; Type: CONSTRAINT; Schema: public; Owner: luis
--

ALTER TABLE ONLY public.branches
    ADD CONSTRAINT branches_pkey PRIMARY KEY (id);


--
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: public; Owner: luis
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (id);


--
-- Name: products products_pkey; Type: CONSTRAINT; Schema: public; Owner: luis
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (id);


--
-- Name: store_products sku_unique; Type: CONSTRAINT; Schema: public; Owner: luis
--

ALTER TABLE ONLY public.store_products
    ADD CONSTRAINT sku_unique UNIQUE (sku);


--
-- Name: store_products stock; Type: CHECK CONSTRAINT; Schema: public; Owner: luis
--

ALTER TABLE public.store_products
    ADD CONSTRAINT stock CHECK ((stock >= 0)) NOT VALID;


--
-- Name: stores store_pkey; Type: CONSTRAINT; Schema: public; Owner: luis
--

ALTER TABLE ONLY public.stores
    ADD CONSTRAINT store_pkey PRIMARY KEY (id);


--
-- Name: store_products store_products_pkey; Type: CONSTRAINT; Schema: public; Owner: luis
--

ALTER TABLE ONLY public.store_products
    ADD CONSTRAINT store_products_pkey PRIMARY KEY (id);


--
-- Name: store_products store_products_product_id_store_id_key; Type: CONSTRAINT; Schema: public; Owner: luis
--

ALTER TABLE ONLY public.store_products
    ADD CONSTRAINT store_products_product_id_store_id_key UNIQUE (product_id, store_id);


--
-- Name: products id_branch_pk; Type: FK CONSTRAINT; Schema: public; Owner: luis
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT id_branch_pk FOREIGN KEY (id_branch) REFERENCES public.branches(id) NOT VALID;


--
-- Name: products id_category_pk; Type: FK CONSTRAINT; Schema: public; Owner: luis
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT id_category_pk FOREIGN KEY (id_category) REFERENCES public.categories(id) NOT VALID;


--
-- Name: store_products product_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: luis
--

ALTER TABLE ONLY public.store_products
    ADD CONSTRAINT product_id_fk FOREIGN KEY (product_id) REFERENCES public.products(id);


--
-- Name: store_products store_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: luis
--

ALTER TABLE ONLY public.store_products
    ADD CONSTRAINT store_id_fk FOREIGN KEY (store_id) REFERENCES public.stores(id);


--
-- PostgreSQL database dump complete
--

