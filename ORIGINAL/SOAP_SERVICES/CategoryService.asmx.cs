using System.Linq;
using System.Collections.Generic;
using System.Web.Services;
using BLL;
using Entities;
using System.Xml.Serialization;

namespace SOAP_SERVICES
{
    /// <summary>
    /// Descripción breve de CategoryService
    /// </summary>
    [WebService(Namespace = "http://tempuri.org/")]
    [WebServiceBinding(ConformsTo = WsiProfiles.BasicProfile1_1)]
    [System.ComponentModel.ToolboxItem(false)]
    // Para permitir que este servicio web se llame desde un script, mediante ASP.NET AJAX, quite el comentario de la siguiente línea.
    // [System.Web.Script.Services.ScriptService]
    public class CategoryService : System.Web.Services.WebService
    {
        private CategoriesLogic _logic = new CategoriesLogic();

        [WebMethod]
        public List<SerializableCategories> GetAllCategories()
        {
            var categories = _logic.RetrieveAll();
            return categories.ConvertAll(c => new SerializableCategories(c));
        }

        [WebMethod]
        public SerializableCategories GetCategoryById(int id)
        {
            return new SerializableCategories(_logic.RetrieveById(id));
        }

        [WebMethod]
        public void CreateCategory(SerializableCategories category)
        {
            _logic.Create(category.ToCategories());
        }

        [WebMethod]
        public void UpdateCategory(SerializableCategories category)
        {
            _logic.Update(category.ToCategories());
        }

        [WebMethod]
        public void DeleteCategory(int id)
        {
            _logic.Delete(id);
        }
    }

    [XmlRoot("Categories")]
    public class SerializableCategories
    {
        public int CategoryID { get; set; }
        public string CategoryName { get; set; }
        public string Description { get; set; }

        public SerializableCategories() { }

        public SerializableCategories(Categories category)
        {
            CategoryID = category.CategoryID;
            CategoryName = category.CategoryName;
            Description = category.Description;
        }

        public Categories ToCategories()
        {
            return new Categories
            {
                CategoryID = this.CategoryID,
                CategoryName = this.CategoryName,
                Description = this.Description
            };
        }
    }
}
