using System.Collections.Generic;
using System.Web.Services;
using BLL;
using Entities;
using System.Xml.Serialization;

namespace SOAP_SERVICES
{
    /// <summary>
    /// Descripción breve de ProductService
    /// </summary>
    [WebService(Namespace = "http://tempuri.org/")]
    [WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1_1)]
    [System.ComponentModel.ToolboxItem(false)]
    // Para permitir que este servicio web se llame desde un script, mediante ASP.NET AJAX, quite el comentario de la siguiente línea.
    // [System.Web.Script.Services.ScriptService]
    public class ProductService : System.Web.Services.WebService
    {
        private ProductsLogic _logic = new ProductsLogic();

        [WebMethod]
        public List<SerializableProducts> GetAllProducts()
        {
            var products = _logic.RetrieveAll();
            return products.ConvertAll(p => new SerializableProducts((Products)p));
        }

        [WebMethod]
        public SerializableProducts GetProductById(int id)
        {
            return new SerializableProducts(_logic.RetrieveById(id));
        }

        [WebMethod]
        public void CreateProduct(SerializableProducts product)
        {
            _logic.Create(product.ToProducts());
        }

        [WebMethod]
        public void UpdateProduct(SerializableProducts product)
        {
            _logic.Update(product.ToProducts());
        }

        [WebMethod]
        public void DeleteProduct(int id)
        {
            _logic.Delete(id);
        }
    }

    [XmlRoot("Products")]
    public class SerializableProducts
    {
        public int ProductID { get; set; }
        public string ProductName { get; set; }
        public int CategoryID { get; set; }
        public decimal UnitPrice { get; set; }
        public int UnitsInStock { get; set; }

        public SerializableProducts() { }

        public SerializableProducts(Products product)
        {
            ProductID = product.ProductID;
            ProductName = product.ProductName;
            CategoryID = product.CategoryID;
            UnitPrice = product.UnitPrice;
            UnitsInStock = product.UnitsInStock;
        }

        public Products ToProducts()
        {
            return new Products
            {
                ProductID = this.ProductID,
                ProductName = this.ProductName,
                CategoryID = this.CategoryID,
                UnitPrice = this.UnitPrice,
                UnitsInStock = this.UnitsInStock
            };
        }
    }
}
