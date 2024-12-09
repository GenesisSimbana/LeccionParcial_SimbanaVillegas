using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using DAL;
using Entities;

namespace BLL
{
    public class CategoriesLogic
    {
        public Categories Create(Categories categories)
        {
            Categories _categories = null;
            using (var repository = RepositoryFactory.CreateRepository())
            {
                Categories _result = repository.Retrieve<Categories>
                    (c => c.CategoryName == categories.CategoryName);
                if (_result == null)
                {
                    _categories = repository.Create(categories);
                }
                else
                {
                    throw new Exception("Categoria ya existe");
                }
            }
            return categories;
        }

        public Categories RetrieveById(int id)
        {
            Categories _categories = null;
            using (var repository = RepositoryFactory.CreateRepository())
            {
                _categories = repository.Retrieve<Categories>(c => c.CategoryID == id);
            }
            return _categories;
        }

        public bool Update(Categories categories)
        {
            bool _updated = false;
            using (var repository = RepositoryFactory.CreateRepository())
            {
                Categories _result = repository.Retrieve<Categories>
                    (c => c.CategoryName == categories.CategoryName);
                if (_result == null)
                {
                    _updated = repository.Update(categories);
                }
                else
                {
                    throw new Exception("Categoria no existe");
                }
            }
            return _updated;
        }

        public bool Delete(int id)
        {
            bool _delete = false;
            var _category = RetrieveById(id);
            if (_category != null)
            {
                using (var repository = RepositoryFactory.CreateRepository())
                {
                    _delete = repository.Delete(_category);
                }
            }
            return _delete;
        }

        public List<Categories> RetrieveAll()
        {
            using (var repository = RepositoryFactory.CreateRepository())
            {
                // Usar una expresión lambda para obtener todas las categorías
                return repository.Filter<Categories>(c => c.CategoryID > 0).ToList();
            }
        }
    }
}
